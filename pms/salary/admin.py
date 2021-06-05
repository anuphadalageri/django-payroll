from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Overtime, Deduction)
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ("empname", "date",'claims','bonus')
    exclude = ('wages',)
    def empname(self,obj):
        return obj.emp.name
    empname.short_description = 'Employee name'

    
    

@admin.register(Overtime)
class OvertimeAdmin(admin.ModelAdmin):
    list_display = ("empname", "month",'OT_shifts','OT_pay')

    def empname(self,obj):
        return obj.emp_id.name
    empname.short_description = 'Employee name'
    
    

@admin.register(Deduction)
class DeductionAdmin(admin.ModelAdmin):
    list_display = ("empname", "month",'total_deductions')

    def empname(self,obj):
        return obj.emp_id.name
    empname.short_description = 'Employee name'

    #exclude=('remaining_shifts',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ("empname", "base_sal",'pay_per_shift')

    def empname(self,obj):
        return obj.employee_name.name
    empname.short_description = 'Employee name'