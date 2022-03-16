from dataclasses import field
from pyexpat import model
from django import forms
from .models import PerguruanTinggi,Fakultas, ProgramStudi, Staff,Gelar

#form perguruan tinggi
class CreatePerguruanTinggiForm(forms.ModelForm):
    class Meta:
        model = PerguruanTinggi
        fields = '__all__'

class UpdatePerguruanTinggiForm(forms.ModelForm):
    class Meta:
        model = PerguruanTinggi
        fields = '__all__'

#form fakultas
class CreateFakultasForm(forms.ModelForm):
    class Meta:
        model = Fakultas
        fields = '__all__'

class UpdateFakultasForm(forms.ModelForm):
    class Meta:
        model = Fakultas
        fields = '__all__'

#programstudi
class CreateProgramStudiForm(forms.ModelForm):
    class Meta:
        model = ProgramStudi
        fields = '__all__'

class UpdateProgramStudiForm(forms.ModelForm):
    class Meta:
        model = ProgramStudi
        fields = '__all__'

#staff
class CreateStaffForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    

    class Meta:
        model = Staff
        exclude=['admin']

    def save(self, commit=True):
        user = super(CreateStaffForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']

        if commit:
            user.save()
        return user

class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude=['admin']

#gelar
class CreateGelarfForm(forms.ModelForm):
    class Meta:
        model = Gelar
        fields = '__all__'

class UpdateGelarfForm(forms.ModelForm):
    class Meta:
        model = Gelar
        fields = '__all__'