
from email import message
from multiprocessing import context
import os
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse

from skpi_management_app.forms import CreatePelatihanMhsForm, UpdateMAhasiswaForm
from .models import CustomUser, Mahasiswa, Pelatihan




def student_home(request):
    mhs_id = get_object_or_404(Mahasiswa,admin=request.user.id)
    #mahasiswa = get_object_or_404(Mahasiswa,admin=request.user.id)
    mahasiswa = Mahasiswa.objects.get(admin=request.user.id)
    pelatihan = Pelatihan.objects.select_related('mahasiswa').filter(mahasiswa_id=mahasiswa)

   #Sessions.objects.filter(affiliation_session__ip_id=X)
    customuser = get_object_or_404(CustomUser,id=request.user.id)
   # pelatihan = get_object_or_404(Pelatihan,mahasiswa=mhs_id)

    context={
        'mahasiswa':mahasiswa,
        'customuser':customuser,
        'pelatihan':pelatihan,
    }
    return render(request,'mahasiswa_template/home_content.html',context)

def view_mahasiswa(request):
    mahasiswa =  mahasiswa = get_object_or_404(Mahasiswa,admin=request.user.id)
    if request.method == 'POST':
        form = UpdateMAhasiswaForm(request.POST,instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Diupdate!')
    
    else:
         form = UpdateMAhasiswaForm(instance=mahasiswa)
    context = {
        'mahasiswa':mahasiswa,
        'form':form,
    } 
    return render(request,'mahasiswa_template/view_mahasiswa_template.html',context)

def mahasiswa_manage_pelatihan(request):
    mahasiswa = Mahasiswa.objects.get(admin=request.user.id)
    pelatihan = Pelatihan.objects.select_related('mahasiswa').filter(mahasiswa_id=mahasiswa)
    print(pelatihan)

    context={
        'pelatihan':pelatihan,
    }
    return render(request,'mahasiswa_template/manage_pelatihan_template.html',context)

def mahasiswa_add_pelatihan(request):
    form_pelatihan = CreatePelatihanMhsForm()
    context={
        'form_pelatihan':form_pelatihan,
    }
    return render(request,'mahasiswa_template/add_pelatihan_template.html',context)

def mahasiswa_add_pelatihan_save(request):
    mhs = Mahasiswa.objects.get(admin_id=request.user.id)
    print(mhs)
    if request.method == 'POST':
        form_pelatihan = CreatePelatihanMhsForm(request.POST, request.FILES)
        if form_pelatihan.is_valid():
            pelatihanForm = form_pelatihan.save(commit=False)
            pelatihanForm.mahasiswa_id = mhs.id
            pelatihanForm.save()
            messages.success(request,'Data Pelatihan Disimpan!')
            return redirect('mahasiswa_add_pelatihan')
        else:
            messages.error(request,'Data Pelatihan Disimpan!')
            return redirect('mahasiswa_add_pelatihan')
    else:
        return redirect('mahasiswa_manage_pelatihan')

def mahasiswa_hapus_pelatihan(request)