from django import forms

from myhash.models import Myhash

class MyhashForm(forms.ModelForm):
    class Meta:
        model = Myhash
        fields = ('msg',)