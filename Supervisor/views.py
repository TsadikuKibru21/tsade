from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from StudentDean.models import Block
from account.models import UserAccount,User
from .models import ProctorSchedule
from django.contrib import messages
# Create your views here.
@login_required(login_url='login_view')
def home(request):
    return render(request,'Supervisor/index.html')
@login_required(login_url='login_view')
def assign_Block(request):
    block=Block.objects.order_by("Block_name")
    proctor=UserAccount.objects.filter(Role_id=4)
    # user=[]
    # for i in proctor:
    #     user1=User.objects.get(id=i.User_id)
    #     user.append(user1.FirstName)
    # print(user)
    context={"Block":block,"Proctor":proctor}
    if request.method =='POST':
        proctor1=request.POST['proctor']
        block1=request.POST['block']
        proctorid=UserAccount.objects.get(username=proctor1)
    
        Blockid=Block.objects.get(Block_name=block1)
        if ProctorSchedule.objects.filter(user_id=proctorid.id).exists() or ProctorSchedule.objects.filter(Block_id=Blockid).count()>=4:
            messages.info(request,"This Proctor is Already Assigned or This Block Has Enuogh Proctor")
            redirect('assign_block')
        else:
            obj=ProctorSchedule()
            obj.user=proctorid
            obj.Block=Blockid
            obj.save()
            messages.info(request,'Proctor Assigned Succesfully...')
            redirect('assign_block')
            # print(Blockid.id)
    
    return render (request,'Supervisor/assign_block.html',context)
@login_required(login_url='login_view')
def proctor_Info(request):
    result=ProctorSchedule.objects.all()
    return render(request,'Supervisor/proctor_info.html',{'Result':result})
@login_required(login_url='login_view')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('index')
