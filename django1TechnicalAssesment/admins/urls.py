from django.urls import path
from . import views

urlpatterns = [
    path("",views.adminhome,name='adminhome'),
    path("adduser",views.adduser,name='adduser'),
    path("listdepartment",views.listdepartment,name='listdepartment'),
    path("deleteDepartment/<int:id>/",views.deleteDepartment,name='deleteDepartment'),
    path("addDepartment",views.addDepartment,name='addDepartment'),
    path("updateDepartment/<int:id>/",views.updateDepartment,name='updateDepartment'),
    path("bookTicket",views.bookTicket,name='bookTicket'),
    path("createTicket",views.createTicket,name='createTicket'),
    path("listTicket",views.listTicket,name='listTicket'),
    path("deleteTicket/<str:id>/",views.deleteTicket,name='deleteTicket'),


    

    




    


] 