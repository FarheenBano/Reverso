from django.contrib import admin
from django.urls import path,include
from ReversoWeb import views
urlpatterns = [
    path("",views.index,name='home'),
    path("job",views.job,name='job'),
    path("testing",views.testing,name='testing'),
    path("fee",views.fee,name='fee'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("free",views.free,name='free'),



]