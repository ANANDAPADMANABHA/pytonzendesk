import json
from bottle import route, template, run, static_file, request
import requests
from django.http import HttpResponse

from urllib import response
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from .models import Department
from authentication.models import  UserAccount



# Create your views here.
@cache_control(no_cache =True, must_revalidate =True, no_store =True)
def adminhome(request):
    if 'username' in request.session:
        return render(request,'index_admin.html')

    else:
        return redirect("adminlogin")

def adduser(request):
    if 'username' in request.session:
        departments = Department.objects.all()
        emailid = "ananthapadmanabhan012@gmail.com"
        if request.method == "POST":
            print("*****************************************")

            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile_number = request.POST.get('mobile_number')
            password = request.POST.get('password')
            role = request.POST.get('role')
            dep = request.POST.get('department')
            print(name,email,mobile_number,password,role,dep)
            print("*****************************************")

            data = {"user": {"name": name, "email": email,'phone':mobile_number }}
            print("*****************************************")

            ticket = json.dumps(data)
            print("*****************************************")

            user = emailid + '/token'
            api_token = 'uzvdcvLh7Y2NPIYWkRgGndb0nJaWjhxRCCb7OkJn'
            url = 'https://shoplifter.zendesk.com/api/v2/users.json'
            headers = {'content-type': 'application/json'}
            print("*****************************************")

            r = requests.post(
                url,
                data=ticket,
                auth=(user, api_token),
                headers=headers
                )
            
           
                
            print(r.json()['user']['id'])
            js = r.json()
            userid = js['user']['id']

            print("**************************************111***")

            if r.status_code != 201:
                if r.status_code == 401 or 422:
                    print("***************if**************************")


                    status = 'Could not authenticate you. Check your email address or register.'
                else:
                    print("****************elst*************************")

                    status = 'Problem with the request. Status ' + str(r.status_code)
                return HttpResponse(status)




            Created_by = request.user
            department = Department.objects.get(id =dep )
            user = UserAccount.objects.create_user(username= name,userid=userid,email = email,phone_number=mobile_number, password = password,role=role,department=department,Created_by=Created_by)
            user.save()

        return render(request,'adduser.html',{"departments":departments})

    else:
        return redirect("adminlogin")


def listdepartment(request):
    if 'username' in request.session:
        dep = Department.objects.all()
        
        return render(request , "department.html",{"dep":dep})
    else:
        return redirect("adminlogin")

def deleteDepartment(request ,id):
    if 'username' in request.session:
        try:
            dep = Department.objects.get(id=id)
            dep.delete()
            return redirect("listdepartment")
        except:
            return render(request,"error_page.html")
    else:
        return redirect("adminlogin")

def addDepartment(request):
    if 'username' in request.session:
        users = UserAccount.objects.all()
       
        
        if request.method == "POST":
            Name = request.POST.get('name')
            Description = request.POST.get('description')
            userid = request.POST.get('Created_by')
            Created_by = UserAccount.objects.get(id = userid )

            
            
            dep = Department(Name= Name,Description = Description,Created_by=Created_by)
            dep.save()
            return redirect("listdepartment")
        return render(request , "adddepartment.html",{"users":users})
    else:
        return redirect("adminlogin")

def updateDepartment(request,id):
    if 'username' in request.session:
        editdep = Department.objects.get(id = id)
        users = UserAccount.objects.all()
        if request.method == 'POST':
            
            name = request.POST.get('name')
            description = request.POST.get('description')
            Created_by_id = request.POST.get('Created_by')
            Created_by = UserAccount.objects.get(id = Created_by_id )

            editdep.Name =name
            editdep.Description =description
            editdep.Created_by =Created_by
            editdep.save()

            return redirect("listdepartment")



        

        return render(request , "editDepartment.html",{"users":users ,"editdep":editdep})
    else:
        return redirect("adminlogin")


def createTicket(request):
    if 'username' in request.session:
        user = request.user
        user_object = UserAccount.objects.get(email = user)
      
        
        if request.method == "POST":

            Subject = request.POST.get('Subject')
            Body = request.POST.get('Body')
            Priority = request.POST.get('Priority')
            email = "ananthapadmanabhan012@gmail.com"
            

            data = {'request': {'subject': Subject, 'comment': {'body': Body}}}
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

            

            
            if r.status_code != 201:
                if r.status_code == 401 or 422:
                    status = 'Could not authenticate you. Check your email address or register.'
                else:
                    status = 'Problem with the request. Status ' + str(r.status_code)
                return status

            return render(request ,"success.html")

        return render(request , "newticket_form.html")


def listTicket(request):
    if 'username' in request.session:
  
        email = "ananthapadmanabhan012@gmail.com"
        user = email + '/token'
        api_token = 'uzvdcvLh7Y2NPIYWkRgGndb0nJaWjhxRCCb7OkJn'
        url = 'https://shoplifter.zendesk.com/api/v2/tickets.json'
       
        
        response = requests.get(url,auth=(user, api_token))
        
        data = response.json()
        print()
        
        return render(request , "listTicket.html",{"data":data['tickets']})

def deleteTicket(request,id):
    if 'username' in request.session:
        email = "ananthapadmanabhan012@gmail.com"
        user = email + '/token'
        api_token = 'uzvdcvLh7Y2NPIYWkRgGndb0nJaWjhxRCCb7OkJn'
        url = 'https://shoplifter.zendesk.com/api/v2/tickets/'+id

        requests.delete(
                url,
                
                auth=(user, api_token),
                
                )

        return redirect("listTicket")

    



        

        
def bookTicket(request):
    

# Set the request parameters
    url = 'https://shoplifter.zendesk.com/api/v2/groups.json'
    user = 'ananthapadmanabhan012@gmail.com'
    pwd = 'qwertyuiop123'
    credentials = (user,pwd)
    session = requests.Session()
    session.auth = credentials
    

    # Do the HTTP get request
    response = session.get(url)
    print(response)
    

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    print("1111111111111111111111111111111111111111111111")

    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    # Example 1: Print the name of the first group in the list
    print( 'First group = ', data['groups'][0]['name'] )

# Example 2: Print the name of each group in the list
    group_list = data['groups']
    for group in group_list:
        print(group['name'])


# class Ticket_Organizations(LoginRequiredMixin, ListView):
#     model = models.Ticket
#     context_object_name = 'Ticket'
#     template_name = 'Ticket/Ticket_organizations.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         user = 'bobbykboseoffice@gmail.com'
#         pwd = 'Password@37'
#         credentials= (user, pwd)
#         session = requests.Session()
#         session.auth = credentials

#         url = 'https://lissah.zendesk.com/api/v2/organizations.json'
#         response = session.get(url)
#         if response.status_code != 200:
#             print(f'Error with status code {response.status_code}')
#             exit()
#         data = response.json()

#         context['Tickets'] = data['organizations']
#         print(data['organizations'])
#         print(data['organizations'].count())
#         print(data['organizations'][0]['name'])


#         context['count'] =  context['Ticket'].count()

#         return context