
from multiprocessing import context
import os
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from .models import Mahasiswa, ProgramStudi


def staff_home(request):
    mahasiswa_count = Mahasiswa.objects.filter(admin_id=request.user.id).count()

    context={
        'mahasiswa_count':mahasiswa_count,

    }
    return render(request,'staff_template/home_content.html',context)