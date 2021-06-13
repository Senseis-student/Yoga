from django.shortcuts import render, redirect
from django.db import models
from . import models


def main(request):
	return render(request, 'program/main.html')

def about(request):
	return render(request, 'program/about.html')

def contact(request):
	return render(request, 'program/contact.html')

def view_program(request):
	program = models.Program.objects.order_by('-id')
	return render(request, 'program/program.html', {'program': program})

def price_list(request):
	program = models.Program.objects.order_by('-id')
	price = models.Price.objects.order_by('-id')
	return render(request, 'program/price.html', {'price':price, 'program': program})