from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .models import Department, Desigination, Employee, Salary
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def login_view(request):
    if request.method== 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        if User.objects.filter(username=username1).exists():
            if Employee.objects.filter(username=username1).exists():
                user = auth.authenticate(username=username1,password=password1)
        else:
            x = Employee.objects.get(username = username1)
            if x.username == username1:
                first_name = x.firstName
                last_name = x.lastName
                username = x.username
                password = x.password
                password2 = x.password
                email = x.email
                user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                user.save();

        if Employee.objects.filter(username=username1).exists():
            user = auth.authenticate(username=username1,password=password1)
        else:
            user = None

        if user is not None:
            auth.login(request, user)
            x = user.username
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'Management/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def change_password(request):
    if request.method == 'POST':
        username = request.POST["username"]
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']

        employee = Employee.objects.get(username = username)
        user = User.objects.get(username=username)

        if username == user.username:
            if currentpassword == employee.password:
                user.password = newpassword
                user.save();
                update_session_auth_hash(request, user)

                employee.password = newpassword
                employee.save();
                return redirect('home')

            else:
                messages.info(request,'Current password is Invalid')
                return redirect('changepassword')
        else:
            messages.info(request,'User name does not exist')
            return redirect('changepassword')
    else:
        return render(request, 'Management/changepassword.html')



def home_view(request):
    return render(request, 'Management/home.html')

def salaryselect_view(request, username):
    years = []
    months= []
    for employee in Employee.objects.all():
        if employee.username == username:
            profile = employee
    for salary in Salary.objects.all():
        if salary.employee == profile:
            if salary.salaryMonth not in months:
                months.append(salary.salaryMonth)
            if salary.salaryyear not in years:
                years.append(salary.salaryyear)

    context = {'employee': profile, 'months' : months , 'years' : years}
    return render(request, 'Management/salaryselect.html', context)

def salarydetails_view(request, username, year, month):
    return render(request,'Management/salarydetails.html')

def profile_view(request, username):
    for employee in Employee.objects.all():
        if employee.username == username:
            employee1 = employee
    context = {'employee': employee1}
    return render(request, 'Management/employee_details.html', context)
