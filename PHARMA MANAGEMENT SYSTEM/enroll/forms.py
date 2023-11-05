from django.core import validators
from django import forms
from .models import User

class DoctorRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['Doctor_name', 'Specialization', 'Openning_time','Closing_time','Doctor_fees']
  widgets = {
   'Doctor_name': forms.TextInput(attrs={'class':'form-control'}),
   'Specialization': forms.TextInput(attrs={'class':'form-control'}),
   'Openning_time': forms.TimeInput(attrs={'class':'form-control'}),
   'Closing_time': forms.TimeInput(attrs={'class':'form-control'}),
   'Doctor_fees' : forms.TextInput(attrs={'class':'form-control'}),
  }
  