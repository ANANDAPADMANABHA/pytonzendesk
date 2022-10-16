from django.urls import path
from . import views

urlpatterns = [
    path("",views.loginadmin,name='adminlogin'),
    path('signout',views.adminLogout,name='signout'),  
    path('loginuser',views.loginuser,name='loginuser'),  
    path('userLogout',views.userLogout,name='userLogout'),  

    


] 