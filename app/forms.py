from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Patient, CheckList, Father, Profile


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = '__all__'


class FatherForm(forms.ModelForm):
    class Meta:
        model = Father
        fields = '__all__'


class ManagerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('patronymic', 'number_phone')