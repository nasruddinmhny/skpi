
import os
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import CustomUser
from .forms import CreateCustomUserForm

from .models import Mahasiswa, ProgramStudi


def staff_home(request):
    mahasiswa_count = Mahasiswa.objects.all().count()
    programstudi = ProgramStudi.objects.all()

    context={
        'mahasiswa_count':mahasiswa_count,
        'programstudi':programstudi,

    }
    return render(request,'staff_template/home_content.html',context)

def manage_mahasiswa(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request,'staff_template/staff_manage_mahasiswa_template.html',{'mahasiswa':mahasiswa})

def add_mahasiswa(request):
    form_mahasiswa = CreateCustomUserForm()
    context={
        'form_mahasiswa':form_mahasiswa,
    }
    return render(request,'staff_template/add_mahasiswa_template.html',context)

def add_mahasiswa_save(request):
    if request.method == 'POST':
        form_mahasiswa = CreateCustomUserForm(request.POST)  
        if form_mahasiswa.is_valid():
            userForm = form_mahasiswa.save(commit=False)
            userForm.user_type = 3 
            userForm.programstudi_id = ProgramStudi.objects.get(id=1)
            userForm.save()
            messages.success(request,'Data User Disimpan')  
            return redirect('staff_add_mahasiswa')
    else:
        form_mahasiswa= CreateCustomUserForm()
        
    context = {
        'form_mahasiswa':form_mahasiswa,
        
    }
    return render(request,'staff_template/add_mahasiswa_template.html',context)
    '''
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
        
      
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        nim = request.POST.get('nim')
        tempatlahir = request.POST.get('tempatlahir')
        tgllahir = request.POST.get('tgllahir')
        #programstudi = ProgramStudi.objects.get(id=request.POST.get('programstudi'))
        
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.mahasiswa(address=address,nim=nim,tempatlahir=tempatlahir,tgllahir=tgllahir,prodi=programstudi)
            user.save()
            messages.success(request, "Data Mahasiswa Di Tambah!")
            return redirect('add_mahasiswa')
        except:
            messages.error(request, "Data Mahasiswa gagal Di Tambah!")
            return redirect('add_mahasiswa')
        '''

def hapus_mahasiswa(request,mahasiswa_id):
    mahasiswa = Mahasiswa.objects.get(admin=mahasiswa_id)
    user = CustomUser.objects.get(id=mahasiswa_id)
    try:
        mahasiswa.delete()
        user.delete()
        messages.success(request, "Data Mahasiswa Dihapus")
        return redirect('staff_manage_mahasiswa')
    except:
        messages.error(request, "Data mahasiswa gagal di hapus!")
        return redirect('staff_manage_mahasiswa')
