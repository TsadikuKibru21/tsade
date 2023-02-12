from django.contrib.auth import authenticate,logout
from django.shortcuts import render, redirect
from .models import UserAccount,User,Role
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import RoleForm,AddUserForm,AddAccountForm
from django.contrib.auth.hashers import make_password
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def adminhome(request):
    return render(request,"account/index.html")
#################Account Managment###############
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='indlogin_viewex')
def accountmanagment(request):
    result=User.objects.order_by("Id_no")
    return render(request,"account/accountmanagment.html",{"User":result})
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
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
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
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
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def GrantRole(request):
    #form=GrantRoleForm(request.POST or None)
    result=UserAccount.objects.order_by("username") 
    return render(request, "account/grantrole.html",{'Account':result})
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def updaterole(request,pk):
    result=UserAccount.objects.get(id=pk)
    result1=UserAccount.objects.all()
    form=AddAccountForm(request.POST or None,instance=result)
    context = { 'res': result,'form':form} 
    if form.is_valid():
        form.save()
        messages.success(request,"Data Updated Succesfully!")
        return render(request ,'account/grantrole.html',{"Account":result1})
    return render(request,'account/updaterole.html',context)
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
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
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def userinfo(request):
    result=User.objects.order_by("FirstName")
    return render(request,"account/viewuserinfo.html",{"User":result})
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
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
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('index')