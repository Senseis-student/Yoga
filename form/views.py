from django.shortcuts import render, redirect
from django.db import models
from . import models
from program.models import Program
from branches.models import Branches


def new_form(request):
    if request.method == 'GET':
        form = models.Form.objects.all()
        bran_list = models.Branches.objects.all()
        program_list = models.Program.objects.all()
        return render(request, 'form/form.html', {'bran_list': bran_list, 'program_list': program_list})

    elif request.method == 'POST':
        form = models.Form.objects.all()
        bran_list = models.Branches.objects.all()
        program_list = models.Program.objects.all()

        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        scale = request.POST['scale']
        number = request.POST['number']
        email = request.POST['email']
        a = models.Form()
        a.name = name
        a.surname = surname
        a.patronymic = patronymic
        a.scale = scale
        a.number = number
        a.email = email
        if a.name!='':
            if a.number!='':
                a.save()
        return render(request, 'form/form.html', {'bran_list': bran_list, 'program_list': program_list})
    return render(request, 'form/form.html')
