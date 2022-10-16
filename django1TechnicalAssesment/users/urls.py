from django.urls import path
from . import views

urlpatterns = [
    path("",views.listUserTickets,name='listUserTickets'),  
    path("userCreateTicket",views.userCreateTicket,name='userCreateTicket'),  



    

    




    


] 