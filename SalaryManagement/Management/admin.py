from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from Management.actions import export_as_csv_action
from django.utils.translation import ugettext_lazy
from Management.models import Desigination, Employee, Salary,TimeSheet, Department

# Register your models here.

class MyAdminSite(AdminSite):

    site_title = ugettext_lazy('My site admin')


    site_header = ugettext_lazy('My administration')


    index_title = ugettext_lazy('Payroll administration')
    admin.site.site_header = "Salary Management Admin"
    admin.site.site_title = "Salary Management Admin Portal"
    admin.site.index_title = "Welcome to Salary Management Portal"
admin_site = MyAdminSite()

class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    date_hierarchy = 'date'
    list_filter = ('employee', 'status')
    actions = [export_as_csv_action("CSV Export", fields=['employee','date','status'])]

class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(TimeSheet,TimesheetAdmin)
admin.site.unregister(Group)
admin.site.register(Desigination)
admin.site.register(Employee)
admin.site.register(Department)
