from django.shortcuts import render, redirect
from .models import UserAccount,User,Role
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RoleForm,GrantRoleForm,AddUserForm
from django.contrib.auth.hashers import make_password
# Create your views here.
@login_required
def adminhome(request):
    return render(request,"account/index.html")
#################Account Managment###############
@login_required
def accountmanagment(request):
    result=User.objects.order_by("Id_no")
    return render(request,"account/accountmanagment.html",{"User":result})
@login_required
def generateuseraccount(request):
    result=User.objects.order_by("Id_no")
    if request.method == "POST":
       selectedusers=request.POST.getlist("users")
       #print(selectedusers)
    count=0 
    
    for rs in selectedusers:
        user=User.objects.get(Id_no=rs)
        useracc=UserAccount()
        username=user.FirstName+user.LastName
        if UserAccount.objects.filter(username=username).exists():
            pass
        else:
            count+=1
            useracc.username=username
            password=make_password(rs)
            useracc.password=password
            useracc.Role_id=2
            useracc.User_id=int(user.id)
            useracc.save()
    if count ==0:
        messages.info(request,"All users Already have An Account!")
    elif count==1:
        mess=str(count)+" User Account is Succesfully created"
        messages.success(request,mess)
    else:
        mess=str(count)+" User's Account is Succesfully created"
        messages.success(request,mess)      
    return render(request,'account/accountmanagment.html',{"User":result})
@login_required
def AddRole(request):
    form=RoleForm(request.POST or None) 
    if request.method =='POST':
        if form.is_valid():
            name=request.POST['R_name']
            print(name)
            if Role.objects.filter(R_name=name).exists():
                messages.info(request,'This Role is Already Registered!...')
            else:
                form.save()
                messages.info(request,'Role Added Sccesfully!...')
        else:
            messages.info(request,'Invalid Form...')         
    return render(request,"account/addrole.html",{'form':form})
def GrantRole(request):
    form=GrantRoleForm(request.POST or None) 
    return render(request, "account/grantrole.html",{'form':form})
def AddUser(request):
    form=AddUserForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            Id_no=request.POST['Id_no']
            if User.objects.filter(Id_no=Id_no).exists():
                messages.info(request,'This User is Already Registered!...')
            else:
                form.save()
                messages.info(request,'User Added Succesfully!...')
                return redirect('Ad_adduser')
        else:
            messages.info(request,'Invalid Form!...')
    return render(request, "account/adduser.html",{'form':form})
def userinfo(request):
    result=User.objects.order_by("FirstName")
    return render(request,"account/viewuserinfo.html",{"User":result})
def deleteuser(request):
    result=User.objects.order_by("FirstName")
    if request.method == "POST":
       selectedusers=request.POST.getlist("users")
       #print(selectedusers)
    count=0 
    for rs in selectedusers:
        user=User.objects.get(Id_no=rs)
        user.delete() 
        count+=1
    mess=str(count)+" User's Deleted Succesfully!..."
    messages.error(request,mess)
    return render(request,"account/viewuserinfo.html",{"User":result})
@login_required
def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('index')