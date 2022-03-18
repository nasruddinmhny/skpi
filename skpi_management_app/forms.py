from dataclasses import field
from pyexpat import model
from django import forms
from .models import Cpl, Organisasi, PerguruanTinggi,Fakultas, ProgramStudi, Staff,Gelar, SubAspekCpl

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

#cpl
class CreateCplForm(forms.ModelForm):
    class Meta:
        model = Cpl
        fields = '__all__'

class UpdateCplForm(forms.ModelForm):
    class Meta:
        model = Cpl
        fields = '__all__'

#cpl
class CreateSubCplForm(forms.ModelForm):
    class Meta:
        model = SubAspekCpl
        fields = '__all__'

class UpdateSubCplForm(forms.ModelForm):
    class Meta:
        model = SubAspekCpl
        fields = '__all__'

#organisasi
class CreateOrganisasiForm(forms.ModelForm):
    class Meta:
        model = Organisasi
        fields = '__all__'
        #fields = ['nama','periode','jabatan','berkaspendukung','images']

class UpdateOrganisasiForm(forms.ModelForm):
    class Meta:
        model = Organisasi
        fields = '__all__'