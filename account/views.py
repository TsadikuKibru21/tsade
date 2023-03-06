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
    Role_list=['Student_Dean','Student','Proctor','Supervisor','Admin','President','Registrar']
    for i in range(7):
        if Role.objects.filter(R_name=Role_list[i]).exists():
            user=Role.objects.get(R_name=Role_list[i])
            print(user.id)
            pass
        else:
            role=Role()
            role.R_name=Role_list[i]
            role.save()
    
    return render(request,"account/index.html")
#################Account Managment###############
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='indlogin_viewex')
def accountmanagment(request):
    result=User.objects.order_by("Id_no")
    user=User.objects.all().count()
    acc=UserAccount.objects.all().count()
    context={"User":result,'AvUser':user,'Account':acc}
    print(user,acc)
    return render(request,"account/accountmanagment.html",context)
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def generateuseraccount(request):
    result=User.objects.order_by("Id_no")
    user=User.objects.all().count()
    acc=UserAccount.objects.all().count()
    context={"User":result,'AvUser':user,'Account':acc}
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
            useracc.Role_id=3
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
    return render(request,'account/accountmanagment.html',context)

@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def GrantRole(request):
    #form=GrantRoleForm(request.POST or None)
    result=UserAccount.objects.order_by("username") 
    if request.method =='POST':
        searched=request.POST['searched']
        if searched =='Student':
            id=3
        elif searched == 'Student_Dean':
            id=2
        elif searched == 'Admin':
            id=1
        elif searched == 'Proctor':
            id=4
        elif searched == 'Supervisor':
            id=5
        elif searched == 'President':
            id=6
        elif searched == 'Registrar':
            id=7
        else:
            id=0
        result=UserAccount.objects.filter(username__contains=searched)| UserAccount.objects.filter(Role=id)
        return render(request, "account/grantrole.html",{'Account':result})
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
                return redirect('Ad_adduser')
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