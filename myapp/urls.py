from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsletterform', views.newsletterform, name='newsletterform'),
    path('contact', views.contact, name='about'),
    path('about', views.about, name='contact'),
    path('QpiAiPro', views.QpiAiPro, name='QpiAiPro'),
    path('QpiAiOpt', views.QpiAiOpt, name='QpiAiOpt'),
    path('QpiAiSense', views.QpiAiSense, name='QpiAiSense'),
    path('QpiAiHardware', views.QpiAiSim, name='QpiAiSim'),
    path('QpiAiMl', views.QpiAiMl, name='QpiAiMl'),
    path('solutions', views.solutions, name='solutions'),
    path('whitepaper', views.whitepaper, name='whitepaper'),
    path('paperfrom', views.paper_form, name='whitepaperform'),
    path('blog', views.blog, name='blog'),
    path('blogdetails1', views.blogdetails1, name='blog1'),
    path('blogdetails2', views.blogdetails2, name='blog2'),
    path('blogdetails3', views.blogdetails3, name='blog3'),
    path('news', views.news, name='news'),
    path('event', views.event, name='event'),
    path('eventdetails1', views.eventdetails1, name='event1'),
    path('carrers', views.carrers, name='carrers'),
    path('contactform', views.contact_us_form, name='carrers'),



    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),


]