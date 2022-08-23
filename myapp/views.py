from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,"Home.html")

def about(request):
    print("about")
    return render(request,"about.html")
def contact(request):
    print("contact")
    return render(request,"contact.html")


def QpiAiPro(request):
    return render(request,"Pro.html")
def QpiAiOpt(request):
    return render(request,"Opt.html")
def QpiAiSense(request):
    return render(request,"Sense.html")
def QpiAiSim(request):
    return render(request,"Hardware.html")
def QpiAiMl(request):
    return render(request,"ML.html")

def whitepaper(request):
    return render(request,"whitepaper.html")


def solutions(request):
    return render(request,"solutions.html")
def news(request):
    return render(request,"news.html")
def blog(request):
    return render(request,"blog.html")
def event(request):
    return render(request,"event.html")

def eventdetails1(request):
    return render(request,"event-details.html")

def carrers(request):
    return render(request,"carrers.html")

def blogdetails1(request):
    return render(request,"blog-details1.html")

def blogdetails2(request):
    return render(request,"blog-details2.html")

def blogdetails3(request):
    return render(request,"blog-details3.html")

@csrf_exempt
def contact_us_form(request):

    name=request.GET.get('name')
    website=request.GET.get('website')
    email=request.GET.get('email')

    description = request.GET.get('description')
    contactus = models.Contactus(name=name,email=email,website=website,description=description)
    contactus.save()
    return HttpResponse("h2")

@csrf_exempt
def paper_form(request):
    paperid=request.GET.get('id')
    firstname=request.GET.get('firstname')
    lastname=request.GET.get('lastname')
    email=request.GET.get('email')
    company=request.GET.get('company')
    jobtitle=request.GET.get('jobtitle')
    country=request.GET.get('country')
    Industry=request.GET.get('Industry')
    Intrests=request.GET.get('Intrests')


    paper=models.paper(paperid=paperid,firstname=firstname,lastname=lastname,email=email,company=company,jobtitle=jobtitle,country=country,Industry=Industry,Intrests=Intrests)
    paper.save()
    return HttpResponse("h2")
    # return JsonResponse({'response_data':'sd'}, status=200)

@csrf_exempt
def newsletterform(request):
    
    email=request.GET.get('email')
   


    newsletter=models.newsletter(email=email)
    newsletter.save()
    return HttpResponse("h2")
    # return JsonResponse({'response_data':'sd'}, status=200)

