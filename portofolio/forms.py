from django.forms import ModelForm
from django import forms
from portofolio.models import *

class FormFoto(ModelForm):
    class Meta:
        model = Foto
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class' : 'form-control'}),
            'keterangan' : forms.Textarea({'class' : 'form-control'}),
        }