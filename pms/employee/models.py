from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import re
from django.core.exceptions import ValidationError
from month.models import MonthField
from django.contrib.auth.models import User
#from .models2 import Worksite
# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=30)
    lname = models.CharField(max_length=30,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sex = models.CharField(max_length=10,help_text="Male or Female")
    doj = models.DateField()
    work = models.ForeignKey('Worksite',on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True)
    base_sal = models.FloatField(default=0)
    supervisor = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    #salary = models.OneToOneField(Salary,on_delete= models.CASCADE,null=True)
    contact = PhoneNumberField(null=True,blank=True,unique=True)
    image = models.ImageField(upload_to="profpics",null=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id','name','doj')
    
    def get_employee(id):
        return Employee.objects.get(id=id)
    
    def clean_fields(self,exclude=None):
        print("Hi in clean")
        pattern = r'[^A-Za-z]'
        flag=False
        msg1=msg2=msg3=''
        if re.findall(pattern,self.name) != [] :
            msg1 = 'Incorrect name'
            flag=True
            #raise ValidationError('Incorrect name')
        if re.findall(pattern,self.lname) != [] :
            msg2 = 'Incorrect lastname'
            flag=True
            #raise ValidationError('Incorrect lastname')
        if self.sex not in ['Male','Female']:
            msg3 = 'Incorrect sex identified'
            flag=True
            #raise ValidationError('Incorrect sex identified')
        if flag:
           raise ValidationError(msg1 +'\n'+msg2+'\n'+msg3) 
class Worksite(models.Model):
    name = models.CharField(max_length=20)       
    location = models.CharField(max_length=20)
    address = models.TextField(max_length=35)
    manager = models.ForeignKey(Employee,on_delete=models.CASCADE)
    contact = PhoneNumberField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    in_time = models.TimeField()
    out_time = models.TimeField()
    #worksite =  models.ForeignKey(Worksite, on_delete = models.CASCADE,null=True)
    class Meta:
        unique_together = ('emp_id','date')
    
   
    @property
    def hours(self):
        end_minutes = self.out_time.hour*60 + self.out_time.minute
        start_minutes = self. in_time.hour*60 + self.in_time.minute
        return round((end_minutes - start_minutes) / 60,2)
    

    def clean_fields(self,exclude=None):
        if self.in_time > self.out_time:
            raise ValidationError("Provide valid time punches")
    def __str__(self):
        return str(self.emp_id.name)+' '+str(self.date)
    
    

class Category(models.Model):
    name = models.CharField(max_length=15)
    num_of_emp = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return str(self.name)

class LabourHour(models.Model):
    date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    worksite =  models.ForeignKey(Worksite, on_delete = models.CASCADE,null=True)
    hours = models.FloatField(default=0)
    overtime_hours=models.IntegerField(default=0)
    unrecorded_hours = models.IntegerField(default=0)
    class Meta:
        unique_together = ('emp_id','date')

    def __str__(self):
        return str(self.emp_id.name)+str(self.date)

class WorkingShift(models.Model):
    month = MonthField(null=False,blank=False)
    worksite = models.ForeignKey(Worksite,on_delete=models.CASCADE, null=False)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE, null=False)
    working_days = models.IntegerField(default=27)
    leaves_allowed = models.IntegerField(default=0)

    class Meta:
        unique_together = ('month','worksite','category')
    
    def __str__(self):
        return "Shift for" +str(self.category.name)+ str(self.month)