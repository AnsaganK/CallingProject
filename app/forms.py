from django import forms

from app.models import Patient, CheckList


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = '__all__'
