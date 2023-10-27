from typing import Dict, Any

from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    loyihalar = Project.objects.all()[:2]
    xizmatlar = Servise.objects.all()[:2]
    contex = {'services': xizmatlar,
              'projects': loyihalar}
    return render(malumot, 'index.html', contex)

def about(malumot):
    haqida = About.objects.all()
    haqidalar = {'haqidalar': haqida}
    return render(malumot, 'about.html', haqidalar)

def blog(malumot):
    return render(malumot, 'blog.html')

def contact(malumot):
    return render(malumot, 'contact.html')

def services(malumot):
    xizmat = Servise.objects.all()
    xizmatlar = {'xizmatlar': xizmat}
    return render(malumot, 'services.html', xizmatlar)

def project(malumot):
    loyiha = Project.objects.all()
    loyihalar = {'loyihalar': loyiha}
    return render(malumot, 'project.html', loyihalar)

def contact_us(malumot):
    name = malumot.POST.get('ism')
    lastname = malumot.POST.get('familiya')
    email = malumot.POST.get('email')
    text = malumot.POST.get('matn')
    Contact(name=name, lastname=lastname, email=email, text=text).save()

    boglanish = Contact.objects.all()
    lugat = {'contact': boglanish}
    return render(malumot, 'contact.html', lugat)
