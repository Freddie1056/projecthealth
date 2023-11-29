from django import forms
from dataapp.models import Patient


class PatientsForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields =['blood_pressure', 'blood_sugar']