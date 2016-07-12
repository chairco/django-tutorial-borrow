# faships/forms.py
from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Faship, Device

from users.models import Pegadri, Cocodri, Functionteam


FashipFormSet = inlineformset_factory(
    Faship, Device, extra=0, min_num=1,
    fields=('isn', 'station', 'radar', 'ffned', 'uifdr')
)


class FashipForm(forms.ModelForm):

    pegadri = forms.ModelChoiceField(
        queryset=Pegadri.objects.exclude(name__istartswith='%').order_by('name'),
        label='Pega DRI',
        help_text='<button type="button" class="btn btn-info btn-xs" data-style="zoom-in"' \
           'data-toggle="modal" data-target="#pegaModal"' \
           'data-whatever="@pega"> <span class="ladda-label">Add PEGA DRI</span></button>'
    )

    cocodri = forms.ModelChoiceField(
        queryset=Cocodri.objects.all().order_by('name'),
        label='CoCo DRI',
        help_text='<button type="button" class="btn btn-info btn-xs" data-style="zoom-in"' \
                  'data-toggle="modal" data-target="#cocoModal"' \
                  'data-whatever="@pega"> <span class="ladda-label">Add CoCo DRI</span></button>'
    )

    pega_dri_mail_group = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Pegadri.objects.all().order_by('name'),
        label='PEGA DRI Mail List',
        help_text='<button type="button" class="btn btn-info btn-xs" data-style="zoom-in"' \
                  'data-toggle="modal" data-target="#pegaModal"' \
                  'data-whatever="@pega"> <span class="ladda-label">Add PEGA DRI</span></button>',
        widget=forms.SelectMultiple(attrs={'size':'10'})
    )

    class Meta:
        model = Faship
        fields = (
            'function_team', 'pegadri', 'cocodri', 
            'recipient', 'pega_dri_mail_group', 'purpose',
        )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        if user.has_perm('users.delete_cocodri'):
          pass
        else:
          self.fields['cocodri'].queryset = Cocodri.objects.filter(owner=user)
        
        if user.has_perm('users.delete_pegadri'):
          pass
        else:
          self.fields['pegadri'].queryset = Pegadri.objects.filter(owner=user)
          self.fields['pega_dri_mail_group'].queryset = Pegadri.objects.filter(owner=user)


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('isn', 'config', 'unit_no',)


