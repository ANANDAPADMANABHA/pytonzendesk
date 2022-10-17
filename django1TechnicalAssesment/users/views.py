from django.shortcuts import render
import json
from urllib import response
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
import requests

from authentication.models import  UserAccount
from authentication.serializers import UserSerializer

# Create your views here.

def listUserTickets(request):
        email = "ananthapadmanabhan012@gmail.com"
        user = email + '/token'
        users = UserAccount.objects.get(email = request.user)
        print("aaaaaaaaaaaaa",users.userid )

        api_token = 'uzvdcvLh7Y2NPIYWkRgGndb0nJaWjhxRCCb7OkJn'
        url = 'https://shoplifter.zendesk.com/api/v2/users/'+ users.userid +'/tickets/requested'
        print(url)
       
        
        response = requests.get(url,auth=(user, api_token))
        
        data = response.json()
        
        print(data,"dataaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        return render(request , "listUserTicket.html",{"data":data['tickets']})




def userCreateTicket(request):
    # if 'username' in request.session:
       
        user = request.user
        user_object = UserAccount.objects.get(email = user)
        objserialise = UserSerializer(user_object)
        
        if request.method == "POST":

            Subject = request.POST.get('Subject')
            Body = request.POST.get('Body')
            Priority = request.POST.get('Priority')
            email = "ananthapadmanabhan012@gmail.com"
            
          

            data = {'request': {'subject': Subject,'comment': {'body': Body},"requester": {  "name": objserialise.data["username"], "email": objserialise.data['email'] }}}
            print(user_object.userid)
            ticket = json.dumps(data)
            user = email + '/token'
            api_token = 'uzvdcvLh7Y2NPIYWkRgGndb0nJaWjhxRCCb7OkJn'
            url = 'https://shoplifter.zendesk.com/api/v2/requests.json'
            headers = {'content-type': 'application/json'}  
            r = requests.post(
                url,
                data=ticket,
                auth=(user, api_token),
                headers=headers
                )

            print(r.json())

            
            if r.status_code != 201:
                if r.status_code == 401 or 422:
                    status = 'Could not authenticate you. Check your email address or register.'
                else:
                    status = 'Problem with the request. Status ' + str(r.status_code)
                return status

            return render(request ,"successuser.html")

        return render(request , "user_new_ticket.html")

