from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.display, name='display'),
    path('index', views.indexcheck, name='indexcheck'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    #path('search', views.search, name='search'),
    path('load',views.loader),
    path('emplogin',views.empview,name='emplogin'),
    path("atdsearch",views.atdsearch),
    path("empatd/<int:id>",views.show_attendance),
    path('empview/<int:num>',views.showtheirinfo)
]