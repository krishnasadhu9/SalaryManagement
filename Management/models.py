from django.db import models
from datetime import datetime
import uuid

Days = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name

class Desigination(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name


class Employee(models.Model):

    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=10,unique=True, default=uuid.uuid4)
    password = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    dob = models.DateField(max_length=8)
    contact = models.CharField(max_length=13, null=True)
    CTC = models.IntegerField("CTC - Yearly", default='0')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=True, null=True)
    desigination = models.ForeignKey(Desigination, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName + "\nUsername : "  + self.username

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None, blank=True, null=True)
    salaryMonth = models.CharField(max_length=10, choices=Days)
    salaryyear = models.IntegerField("Salary Year")
    working_days = models.IntegerField("No. of working days")
    working_days_worked = models.IntegerField("No. of days worked")
    other_allowances = models.FloatField("Other Allowances")


    def __str__(self):
        return self.employee.firstName + " " + self.employee.lastName + " \nMonth : " + self.salaryMonth + "\nYear : " + str(self.salaryyear)


    def salary_calculation(self):
        self.CTC = self.employee.CTC
        self.Monthly_salary = int(self.CTC) // 12
        self.basic_salary = self.Monthly_salary
        self.da_salary = self.basic_salary * 0.20
        self.hra_salary = self.basic_salary * 0.50
        self.ca_salary = 800
        self.total_earning = self.basic_salary + self.hra_salary + self.da_salary + self.ca_salary + self.other_allowances
        st = "*************************************************************************"
        st = st + "\nSALARY STRUCTURE for the Month : " + str(self.salary_month) + " and Year : " + str(
            self.salary_year) + " for Employee :\n" + str(
            self.emp)
        st = st + "\n\nSALARY STATEMENT :\nCTC per year : $ " + str(self.CTC)
        st = st + "\nCTC per month : $ " + str(self.Monthly_salary)
        st = st + "\n\nEARNINGS : \nBasic : $ " + str(self.basic_salary)
        st = st + "\nDearness Allowance(DA) : $ " + str(self.da_salary)
        st = st + "\nHouse Rent Allowance(HRA) : $ " + str(self.hra_salary)
        st = st + "\nConveyance Allowance(CA) : $ " + str(self.ca_salary)
        st = st + "\nOther Allowance : $ " + str(self.other_allowances)
        st = st + "\nTotal Earning : $ " + str(self.total_earning)

        # Deduction Summary
        self.pf_salary = (self.basic_salary + self.da_salary) * 0.12
        self.pt_salary = self.total_earning * 0.005
        self.td_salary = 12500 + ((self.CTC * 0.20) // 12)
        self.total_deductions = self.pf_salary + self.pt_salary + self.td_salary
        self.total = self.total_earning - self.total_deductions
        st = st + "\n\nDEDUCTIONS : \nProvident Fund(PF) : $ " + str(self.pf_salary)
        st = st + "\nProfessional Tax(PT) : $ " + str(self.pt_salary)
        st = st + "\nTax Deducted(Tax) : $ " + str(self.td_salary)
        st = st + "\nTotal Deductions : $ " + str(self.total_deductions)
        st = st + "\nTotal Take-away Salary : $ " + str(self.total)


        self.no_of_days_leave = self.working_days - self.working_days_worked
        # break
        self.amount_to_deduct_for_leave = (self.total // self.working_days) * self.no_of_days_leave
        st = st + "\n\nLEAVE DETAILS : \nNumber of working days : " + str(self.working_days)
        st = st + "\nNumber of days leave : " + str(self.no_of_days_leave)
        st = st + "\nAmount to be deducted : $ " + str(self.amount_to_deduct_for_leave)
        self.nettotal = self.total - self.amount_to_deduct_for_leave
        st = st + "\nNet Take-away Salary : $ " + str(self.nettotal)
        st = st + "\n\n*************************************************************************"
        self.statement = st
        return "Salary Calculated. Here are the details : "
