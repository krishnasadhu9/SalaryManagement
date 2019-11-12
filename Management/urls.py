from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [


path("login",views.login_view, name="login"),
path("logout", views.logout, name="logout"),
path("details/<str:username>",views.profile_view, name="profile"),
path("salaryselect/<str:username>", views.salaryselect_view, name="select"),
path("home", views.home_view, name = "home"),
path("salarydetails/<str:username>/<int:year>/<str:month>", views.salarydetails_view, name = "salarydetails"),
path("changepassword", views.change_password, name = "changepassword")

]
