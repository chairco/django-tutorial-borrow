# loans/forms.py
from django import forms
from django.forms.models import inlineformset_factory
from .models import Loan, Device

from users.models import Pegadri, Cocodri, Functionteam

class LoanForm(forms.ModelForm):

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
        model = Loan
        fields = ('function_team', 'pegadri', 'cocodri', 'purpose', )


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('isn', 'config', 'unit_no')


LoanFormSet = inlineformset_factory(
    Loan, Device,
    extra=0,
    min_num=1,
    fields=('isn', 'config')
)
