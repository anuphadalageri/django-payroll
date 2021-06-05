from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from .models import * #Employee, Attendance, Worksite, Category
import datetime as dt
from django.http import Http404
from salary.models import Payroll, Overtime
import month
#import Exception
# Create your views here.

def display(request):
    '''print(request.user)
    group = Group.objects.get(name="Employee") 
    print(group)
    print(group in Group.objects.all())
    if request.user=="AnonymousUser":
       return render(request,'index.html') 
    try:
        if group in Group.objects.all():
            print("An employee")
            return render(request,'employee.html')
        else:
            print("Not an employee")
    except Exception as e:
        print("Exception")
        print(e)
        print(request.user)'''
    

    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        pd1 = request.POST['psd']
        pd2 = request.POST['cpsd']
        mail = request.POST['mail']
        un = request.POST['user_name']
       # user = User.objects.create_user()
       # user.save()
        msg =""
        if pd1 == pd2:
            if User.objects.filter(username=un).exists():
                msg = "Uname exists"
            elif User.objects.filter(email = mail).exists():
                msg = 'Mail exists'
                print("Mail exists")
            else:
                user = User.objects.create_user(username = un,first_name=fn,last_name=ln,\
                email=mail,password=pd1)
                user.save()
                print("User created")
                auth.login(request,user)
                return redirect('/')
        else:
           msg ="Passwords dont match"
        messages.info(request,msg)
        return redirect("register")
        
        
    else:
        return render(request,'userform.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        psd = request.POST['psd']

        user  = auth.authenticate(username = uname, password =psd)
        print(user)
        if user!=None:
            auth.login(request,user)
            return redirect('/emplogin')
        else:
            messages.info(request,"Incorrect username or password")
            return redirect('login')
    else:
        return render(request,'login.html')
'''
def create_emp(request):
    msg=''
    try:
        val = request.POST['val']
        if val==1:
            emp = Employee()
            emp.name="Ramadas"
            emp.sex='Male'
            emp.doj = datetime.date
            emp.save()
            msg = 'Successfull'
            print('DONE')
            #logout(request)
    except Exception as er: #MultiValueDictKeyError
        msg = 'In exception'
    messages.info(request,msg)
    return render(request,'emp.html')'''

def search(request):
    name = request.POST['search']
    try:
        #Better for prefixes
        obj = Employee.objects.filter(name__icontains=name)[0]  
        atd = Attendance.objects.filter(emp_id= obj.id)
        return render(request,'details.html',{'obj':obj,'atd':atd})
    
    except Exception as e:
        exc = "No employee named " + name
        print(e)
        #return render(request, 'exception.html',{'exc':exc})
        messages.info(request, exc)
        return redirect('/')

def loader(request):
    
    #atd = Attendance.objects.filter(date='2020-12-4')
    '''mont = dt.date.today().month-1
    year = dt.date.today().year
    m = month.Month(year,mont)
    atd= LabourHour.objects.all().filter(emp_id=2,date__month=\
            mont)
    obj = atd.count()
    query = atd.query'''
    '''obj=Attendance.objects.filter(emp_id=2,date__month=11)
    query =obj.query'''
    #obj = Employee.objects.all().filter(name__icontains='ven') name pattern
    obj= Payroll.objects.all().filter(emp=2,date__month=11)
    query=obj.query
    query = str(query)
    query = query.replace('`',"")
    return render(request,'load.html',{'query':query,'obj':obj})
    #return render(request,'index1.html')

def show_attendance(request,id):
    emp = Employee.objects.get(pk=id)
    print(emp.name)
    atd = Attendance.objects.filter(emp_id=id)
    #emp = Employee.objects.get(pk=id)
    print(atd)
    return render(request,'detailsview.html',{'objects':atd,"emp":emp,"num1":1})

def empview(request):

    if request.user.is_authenticated:
        print("Yes")
        emp = Employee.objects.get(pk=2)
        return render(request,'employee.html',{'emp':emp})
    else:
        print('No')
        raise Http404
        
        return None

def atdsearch(request):
    if request.method=='POST':
        name = request.POST['search']
        emp = Employee.objects.all().filter(name__icontains=name)
        
        print(emp)
        if len(emp)==0:
            messages.info(request,"Could not find any employee named "+name)
        else:
            messages.info(request,"Results")
        return render(request,'attendanceresults.html',{'obj':emp})
    else:
        return redirect('/')

def showtheirinfo(request,num):
    uname = request.user
    emp_id = Employee.objects.get(username=uname)
    print(has_group(request.user,"Employee"))
    id = emp_id.id
    if num==1 :
        date = request.POST['date']
        date = date.split('-')
        print(date[1])  #month
        #show_attendance(request,emp_id)
        #print('Emp name ',id.name)
        atd = Attendance.objects.filter(emp_id=id,date__month=date[1])
        emp = Employee.objects.get(pk=id)
        #hours = [(a.out_time - a.in_time)%60 for a in atd]
        hours = [a.hours for a in atd]
        print("Hours: ",hours)
        print(emp.name)
        print(atd)
        return render(request,'detailsview.html',{'objects':atd,"emp":emp,'num1':num})
    elif num==2:
       # payroll = Payroll.objects.all().get(emp=id,date=dt.date(2020,12,24))
        date = dt.date.today()
        mont = date.month

        #payroll = Payroll.objects.all().get(emp=id,date=dt.date(2020,12,24))
        payroll = Payroll.objects.all().filter(emp=id,date__month=mont)
        if(payroll.count()>1):
            payroll=payroll[1]
        else:
            payroll= payroll[0]
        return render(request,'detailsview.html',{'obj':payroll,'num2':num})
    elif num==3:
        mont = dt.date.today().month
        year = dt.date.today().year
        m = month.Month(year,mont)
        #ot = Overtime.objects.get(id=4)
        ot = Overtime.objects.filter(emp_id=id,month=m)
        print(ot)
        
        return render(request,'detailsview.html',{'obj':ot,'num3':num})
    else:
        return redirect('/')
def handle404(request,exception):
    return render(request,'404.html')
def handle500(request):
    return render(request,'404.html')

def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def indexcheck(request):
    print(request.user)
    group = Group.objects.get(name="Employee") 
    print(request.user.groups.all())
    print(group in request.user.groups.all())
    
    try:
        if group in request.user.groups.all():
            print("An employee")
            return render(request,'employee.html')
        else:
            print("Not an employee")
    except Exception as e:
        print("Exception")
        print(e)

    return render(request,'index.html')