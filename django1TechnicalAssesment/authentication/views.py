from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import cache_control




# Create your views here.

@cache_control(no_cache =True, must_revalidate =True, no_store =True)
def loginadmin(request):
    if 'username' in request.session:
        return redirect("adminhome")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username,password=password)

        if user is not None:
            if user.is_superuser:
                request.session['username']=username
                login(request,user)
                return redirect("adminhome")
        else:
            messages.error(request,'invalid credentials')
            return redirect(loginadmin)

    return render (request,'adminlogin.html')


def adminLogout(request):
    if 'username' in request.session:
        request.session.flush()
    logout(request)
    return redirect(loginadmin)


def loginuser(request):
    if 'username' in request.session:
        return redirect("adminhome")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username,password=password)

        if user is not None:
            
                request.session['username']=username
                login(request,user)
                return render(request,"userHome.html")
        else:
            messages.error(request,'invalid credentials')
            return redirect(loginuser)

    return render (request,'userLogin.html')

def userLogout(request):
    if 'username' in request.session:
        request.session.flush()
    logout(request)
    return redirect(loginuser)