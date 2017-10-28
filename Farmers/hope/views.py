# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.





def Gov_login(request):
	 return render(request, 'hope/Gov_login.html')
def index(request):
	 return render(request, 'hope/index.html')
def farmers_login(request):
	return render(request, 'hope/farmers_login.html')
def gov_scheme(request):
	return render(request, 'hope/gov_scheme.html')
def farmers_signup(request):
	return render(request, 'hope/farmers-signup.html')


	
