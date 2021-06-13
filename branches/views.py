from django.shortcuts import render, redirect
from django.db import models
from . import models


def view_branches(request):
	branches = models.Branches.objects.order_by('-id')
	return render(request, 'branches/branches.html', {'branches': branches})
