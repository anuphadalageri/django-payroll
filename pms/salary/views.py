import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from io import BytesIO
import base64
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from employee.models import Employee, Attendance
from .models import *
import datetime as dt

#from .classes import Payslip
# Create your views here.
def display(request):
    return render(request,'page.html')
'''
def edit_sal(request):
    if(request.method == 'GET'):
        #obj = Salary.objects.get(id=1)
        obj = Salary(emp=Employee.objects.get(id=1),date=dt.date.today())
        obj.save()
        return render(request,'edit.html',{'obj':obj})
    else:
        try:
            #wage = request.POST['wage']
            id = request.POST['id']
            claims = request.POST['claims']
            bonus = request.POST['bonus']
            obj = Salary.objects.get(emp=1,date=dt.date.today())
            
            if(obj.emp.base_sal!=wage):
               obj.emp.base_sal=wage
               obj.emp.save()
            obj.claims=claims
            obj.bonus=bonus
            obj.save()
            msg = "Salary updated"
        except Exception as e:
            msg='Failed to update'
        messages.info(request,msg)
        return redirect('/salary')

'''

def payslip(request,id):
    #id =2 #venki
    '''
    emp = Employee.objects.get(pk=id)
    salary = Salary.objects.get(employee_name=emp.id)
    overtime = 2'''
    date = dt.date.today()
    month = date.month

    #payroll = Payroll.objects.all().get(emp=id,date=dt.date(2020,12,24))
    payroll = Payroll.objects.all().filter(emp=id,date__month=month)
    if(payroll.count()>1):
        payroll=payroll[1]
    else:
        payroll= payroll[0]
    print(payroll.deduction.total_deductions)
    print(payroll.amount)


    return render(request,'payroll.html',{'obj':payroll})

def show(request):
    return render(request,'features.html')

def search(request):
    if request.method=='POST':
        name = request.POST['search']
        emp = Employee.objects.all().filter(name__icontains=name)
        print(emp)
        return render(request,'searchresults.html',{'obj':emp})
    else:
        return redirect('/')

def salaryslip(request,id):
    #obj = Employee.objects.get(pk=id)
    date = dt.date.today()
    month=date.month
    time = dt.datetime.now().strftime("%H:%M:%S")
    print(month,id,dt.datetime.now())
    obj = Payroll.objects.get(emp=id,date__month=month)
    print("Salaryslip:",obj)
    return render(request,'salaryslip.html',{'obj':obj,'date':date,'time':time})

def loadatd(request):
    return render(request,'attendance.html')

def accountant(request):
    '''if request.user.groups.filter(name=user.name).exists():
        print("YEs")''' #to check if user belongs to group
    if request.user.is_authenticated:
        return render(request,'accountant.html')
    else:
        return redirect("/admin")

def innovative(request):
    if request.method =="POST":
        yr = request.POST['years']
    import warnings
    warnings.filterwarnings('ignore')
    import numpy as np
    import pandas as pd
    #import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    import statsmodels.api as sm

    data = pd.read_csv('Salary_Data.csv')
    #query = sns.pairplot(y_vars = 'Salary', x_vars = 'YearsExperience' ,data = data)
    X = data['YearsExperience']
    y = data['Salary']
    X_train,X_test,y_train, y_test = train_test_split(X,y, train_size = 0.7, test_size = 0.3, random_state = 100)
    X_train_sm = sm.add_constant(X_train)
    model = sm.OLS(y_train, X_train_sm).fit()
    yr = float(yr)
    y = int(yr)
    ans =model.predict([0,y])
    plt.scatter(X_train,y_train)
    plt.plot(X_train, 25200 + X_train * 9731.2038,'r')
    #plt.show()
    plt.title("Correlation between Salary and years of Experience")
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()
    print("Hello, ans: ",ans,ans[0])
    obj=ans[0]
    obj= round(obj,2)
    return render(request,'features.html',{'sal':obj,'year':yr,'img':image_base64})