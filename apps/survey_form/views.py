from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'survey_form/index.html')

def display_result(request):
    return render(request, 'survey_form/results.html')

def process_form(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['tries'] += 1
    return redirect('/result')