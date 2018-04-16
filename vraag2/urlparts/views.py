# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

para_list = []

# Create your views here.
def param1(request, para):

    response = para        

    para_list.append(response)

    return render(request, 'urlparts/index.html', {'para_list': para_list})

def param2(request, para, para2):

    response = para + " -- " + para2

    para_list.append(response)

    return render(request, 'urlparts/index.html', {'para_list': para_list})

def param3(request, para, para2, para3):

    response = para + " -- " + para2 + " -- " + para3

    para_list.append(response)

    return render(request, 'urlparts/index.html', {'para_list': para_list})
    
def param4(request, para, para2, para3, para4):

    response = para + " -- " + para2 + " -- " + para3 + " -- " + para4

    para_list.append(response)

    return render(request, 'urlparts/index.html', {'para_list': para_list})