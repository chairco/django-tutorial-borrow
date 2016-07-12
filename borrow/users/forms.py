# users/forms.py
from django import forms

from .models import Pegadri, Cocodri, Functionteam


class AddpegadriForm(forms.ModelForm):
    class Meta:
        model = Pegadri
        fields = ('name', 'email')
        labels = {
            'name': 'PEGA DRI NAME',
            'email':  'PEGA DRI EMAIL'
        }
        help_texts = {
            'name': '請勿輸入全型字型例如:錯誤:％, 正確:%.',
            'email': '請勿輸入全型字型例如:錯誤:％, 正確:%.'
        }


class AddcocodriForm(forms.ModelForm):
    class Meta:
        model = Cocodri
        fields = ('name', 'email')
        labels = {
            'name': 'COCO DRI NAME',
            'email':  'COCO DRI EMAIL'
        }
        help_texts = {
            'name': '請勿輸入全型字型例如:錯誤:％, 正確:%.',
            'email': '請勿輸入全型字型例如:錯誤:％, 正確:%.'
        }