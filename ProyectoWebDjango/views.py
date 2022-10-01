from django.shortcuts import render
from django.http import HttpResponse


def cover (request):
    return render(request, 'cover.html')