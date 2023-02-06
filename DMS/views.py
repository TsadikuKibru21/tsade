from account.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import User,Role,UserAccount
from django.contrib.auth.hashers import make_password
def index(request):
    if User.objects.filter(Id_no='Admin').exists():
        print("user already created")
        pass
    else:
        user=User()
        user.FirstName="Admin"
        user.LastName="Admin"
        user.Id_no="Admin"
        user.Gender="Male"
        user.phone_no="123"
        user.save()
        print("user Saved")
    if Role.objects.filter(R_name="Admin").exists():
        print("role already added")
        pass
    else:
        role=Role()
        role.R_name="Admin"
        role.save()
        print("role added")
    if UserAccount.objects.filter(username="Admin").exists():
        print("acc already added")
        pass
    else:
        acc=UserAccount()
        acc.username="Admin"
        password=make_password("Admin")
        acc.password=password
        user=User.objects.get(Id_no="Admin")
        #user1=int(user.id)
        #acc.User=user1
        #acc.save()
        #print("accc added ",user1)
    return render(request,"index.html")
def login_view(request):
    form=LoginForm(request.POST or None)
   
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            
            if user is not None:
                #role=user.Role
                role=str(user.Role)
               
                if role  == "Student_Dean":
                    login(request, user)
                    return redirect('studentdeanhome')
                elif role=='Admin':
                    print(role)
                    login(request, user)
                    request.session['username'] = username
                    
                    print("gate")
                    return redirect('LAdmin',)
                    #return render(request, 'account/index.html',{'username':username})
                elif role=='Student':
                    login(request,user)
                    return redirect('student')
                    #return render(request, 'account/index.html')
                else:
                    print("In cant sign")
            else:
                messages.error(request,"Invalid credientials...")
                 
    return render(request,'login.html',{'form':form})