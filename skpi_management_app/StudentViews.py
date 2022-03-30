
from multiprocessing import context
import os
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse

from skpi_management_app.forms import UpdateMAhasiswaForm
from .models import CustomUser, Mahasiswa, Pelatihan




def student_home(request):
    mahasiswa = get_object_or_404(Mahasiswa,admin=request.user.id)
    customuser = get_object_or_404(CustomUser,id=request.user.id)

    context={
        'mahasiswa':mahasiswa,
        'customuser':customuser,
        

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
    pelatihan = Pelatihan.objects.select_related('mahasiswa').get(mahasiswa=request.user.id)

    context={
        'pelatihan':pelatihan,
    }
    return render(request,'mahasiswa_template/manage_pelatihan_template.html',context)