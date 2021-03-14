from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns=[
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('search',views.search,name="search"),
    path('handlesignup',views.handlesignup,name='handlesignup'),
    path('handlelogin',views.handlelogin,name='handlelogin'),
    path('handlelogout',views.handlelogout,name='handlelogout'),

]