from django.contrib.auth import authenticate,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from StudentDean.models import Placement
from account.models import UserAccount,User
from django.contrib import messages
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def home(request): 
    
    return render(request,'Student/index.html')
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def viewdorm(request):
    if 'username' in request.session:
        username = request.session['username']
        acc=UserAccount.objects.get(username=username)
        user=acc.User_id
        user=User.objects.get(id=user)
        userid=user.Id_no
        if Placement.objects.filter(Stud_id=userid).exists():
            dorm=Placement.objects.get(Stud_id=userid)
            dorm1={'Block':dorm.block ,'Dorm':dorm.room,'Firstname':dorm.FirstName,'Lastname':dorm.LastName}
            return render(request,'Student/viewdorm.html',dorm1)
        else:    
            messages.error(request,"You are Not Assigned Dorm Yet")
    else:
        return redirect('login_view')

    return render(request,'Student/viewdorm.html')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('index')