from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Supervisor.models import ProctorSchedule
# Create your views here.
@login_required(login_url='login_view')
def index(request):
    return render(request,"Proctor/index.html")
@login_required(login_url='login_view')          
def student_info(request):
    if 'username' in request.session:
        username = request.session['username']
    
        proctor=ProctorSchedule.objects.get(user=username)
        print(proctor.Block)

    return render(request,'Proctor/student_info.html')
@login_required(login_url='login_view')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('index')