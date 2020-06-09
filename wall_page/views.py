from django.shortcuts import render, redirect
from django.db.models import Q
from operator import attrgetter
from django.contrib import messages
from .models import Job




def index(request):
    jobs = Job.objects.all()  
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        jobs = jobs.filter(title__icontains=search_term)
    
    context = {'jobs' : jobs, 'search_term': search_term}



    return render(request, "index.html", context) 


def new_job(request):
    return render(request, "add_job.html")

def create_new_job(request):
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add-new')
    
    job = Job.objects.create(title=request.POST['title'], location=request.POST['location'], description = request.POST['description'])
    return redirect("/")

