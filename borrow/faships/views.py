#  faships/views.py
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from .models import Faship

from .forms import FashipForm, DeviceForm, FashipFormSet
from users.forms import AddpegadriForm, AddcocodriForm


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)

        formp = self.get_formp()
        formc = self.get_formc()

        return self.render_to_response(
            self.get_context_data(
                form=form, formset=formset, formp=formp,
                formc=formc
            )
        )

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        
        if form.is_valid() and formset.is_valid():
            return self.form_valid(request, form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formp(self):
        return self.formp

    def get_formc(self):
        return self.formc

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(FormsetMixin, self).get_form_kwargs(*args, **kwargs)
        if self.request.user.is_authenticated():
            form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, request, form, formset):
        faship = form.save(commit=False)
        if request.user.is_authenticated():
            faship.owner = request.user
            
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class FashipCreateView(FormsetMixin, CreateView):
    template_name = 'faships/faship_formset.html'
    model = Faship
    form_class = FashipForm
    formset_class = FashipFormSet
    formp = AddpegadriForm
    formc = AddcocodriForm


class FashipUpdateView(FormsetMixin, UpdateView):
    from django.http import Http404
    template_name = 'faships/faship_formset.html'
    is_update_view = True
    model = Faship
    form_class = FashipForm
    formset_class = FashipFormSet
    formp = AddpegadriForm
    formc = AddcocodriForm

    @method_decorator(permission_required('faships.delete_loan', login_url='/accounts/login/'))
    def dispatch(self, *args, **kwargs):
        return super(FashipUpdateView, self).dispatch(*args, **kwargs)


class FashipList(ListView):

    model = Faship


class FashipDetail(DetailView):

    model = Faship

