from django.shortcuts import render
from .models import Certificates,Contact,Project,Skill

def home(request):
    return render(request, 'home.html', {
        "certificates" : Certificates.objects.all(),
        "contact": Contact.objects.all(),
        "projects" : Project.objects.all(),
        "skills" : Skill.objects.all()
    })