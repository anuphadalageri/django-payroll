from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.display, name='display'),
    #path('editsal',views.edit_sal,name='editsal')
    path('viewsal/<int:id>',views.payslip,name='viewsal'),
    path('salary',views.show,name='salary'),
    path('search',views.search,name='searchsal'),
    path('salaryslip/<int:id>',views.salaryslip,name='salaryslip'),
    path('attendance',views.loadatd,name='attendance'),
    path('accountant',views.accountant,name='accountant'),
    path('innovative',views.innovative,name='innovative')
]