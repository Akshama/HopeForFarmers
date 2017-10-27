# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse("Hope :)")

def Gov_login(request):
	 return render(request, 'hope/Gov_login.html')
def index(request):
	 return render(request, 'hope/index.html')

	
