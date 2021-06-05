from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name",'doj','worksite')
    exclude = ('base_sal',)
    def worksite(self,obj):
        site = obj.work

        return site.name
    worksite.short_description = "Worksite"

@admin.register(Worksite)
class WorksiteAdmin(admin.ModelAdmin):
    list_display = ( "name",'location','man_name')
    def man_name(self,obj):
        man = obj.manager

        return man.name
    man_name.short_description = "Manager"

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("date", "emp_name",'in_time','out_time')

    def emp_name(self,obj):
        emp = obj.emp_id

        return emp.name
    emp_name.short_description = "Name"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(LabourHour)
class LabourHourAdmin(admin.ModelAdmin):
    list_display = ("date","emp_id", 'worksite','hours','overtime_hours'\
        ,'unrecorded_hours')

@admin.register(WorkingShift)
class WorkingShiftAdmin(admin.ModelAdmin):
    list_display = ('month','work','cat','days')

    def work(self,obj):
        return obj.worksite.name
    
    def cat(self,obj):
        return obj.category.name

    def days(self, obj):
        return obj.working_days
    
    cat.short_description='Category'
    work.short_description='Worksite'
    days.short_description='No. of working days'