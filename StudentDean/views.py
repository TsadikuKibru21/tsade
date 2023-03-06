from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from account.models import User,UserAccount
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib import messages
from .serializers import BlockSerializer,DormSerializer,PlacementSerializer,UserSerializer,SaveFileSerializer,UserUploadSerializer
from rest_framework.renderers import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='login_view')
def home(request):
    return render(request, 'Sdeanindex.html')
################USER MANAGEMENT################
def addEmployee(request):
    form=EmployeeForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            Id_no=request.POST['Id_no']
            if User.objects.filter(Id_no=Id_no).exists():
                messages.info(request,'This User is Already Registered!...')
                return redirect('addemployee')
            else:
                form.save()
                messages.info(request,'User Added Succesfully!...')
                return redirect('addemployee')
        else:
            messages.info(request,'Invalid Form!...')
    return render(request,'StudentDean/Employee_Register.html',{'form':form})
#################DORMITORY###############
@login_required(login_url='login_view')
def BlockAdd(request):
    form=AddBlockForm1(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            block=request.POST['Block_name']
            if Block.objects.filter(Block_name=block).exists() :
                messages.error(request, "This Block is already Registerd")
                return redirect('blockadd')
            else:
                form.save()
                messages.success(request,"Block Registered Succesfully")
                return redirect('blockadd')
    return render(request,'StudentDean/addblock.html',{'form':form})
@login_required(login_url='login_view')
def add_dorm(request):
    form=AddDorm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            block=request.POST['Block']
            dorm=request.POST['Dorm_name']
            count_dorm=Dorm.objects.filter(Block_id=block).count()
            block1=Block.objects.get(id=int(block))
            block_capacity=block1.Block_Capacity
            if count_dorm<block_capacity:
                if Dorm.objects.filter(Dorm_name=dorm,Block=block).exists() :
                    messages.error(request, "This Dorm is already Registerd")
                    return redirect('add_dorm')
                else:
                    form.save()
                    messages.success(request,"Dorm Registered Succesfully")
                    return redirect('add_dorm')
            else:
                messages.info(request,"This Block Full You Can't Add Dorm")
                return redirect('add_dorm') 
    return render(request,'StudentDean/add_dorm.html',{'form':form})
@login_required(login_url='login_view')
def viewblock(request):
    result=Block.objects.order_by('Block_name')
    return render(request ,'StudentDean/viewblock.html',{"Block":result})
@login_required(login_url='login_view')
def viewdorm(request,pk):
    result=Dorm.objects.filter(Block=pk)
    #result=Dorm.objects.order_by('Block')
    return render(request ,'StudentDean/viewdorm.html',{"Dorm":result })
@login_required(login_url='login_view')
def updateblock(request,pk):
    result=Block.objects.get(id=pk)
    result1=Block.objects.all()
    form=AddBlockForm(request.POST or None,instance=result)
    context = { 'res': result,'form':form} 
    if form.is_valid():
        form.save()
        messages.success(request,"Data Updated Succesfully!")
        return render(request ,'StudentDean/viewblock.html',{"Block":result1})
    return render(request,'StudentDean/updateblock.html',context)
@login_required(login_url='login_view')
def updatedorm(request,pk):
    result=Dorm.objects.get(id=pk)
    result1=Dorm.objects.order_by('Block')
    form=AddDorm(request.POST or None,instance=result)
    context = { 'res': result,'form':form} 
    if form.is_valid():
        form.save()
        messages.success(request,"Data Updated Succesfully!")
        return render(request ,'StudentDean/viewdorm.html',{"Dorm":result1})
    return render(request,'StudentDean/updatedorm.html',context)
@login_required(login_url='login_view')
def delatedorm(request,pk):
    result=Dorm.objects.get(id=pk)
    result1=Dorm.objects.order_by('Block')
    result.delete() 
    messages.error(request,"Data Deleted Succesfully!")
    return redirect('viewdorm')
@login_required(login_url='login_view')
def delateblock(request,pk):
    result=Block.objects.get(id=pk)
    result1=Block.objects.order_by('Block_name')
    result.delete() 
    messages.error(request,"Data Deleted Succesfully!") 
    return redirect('viewblock')

############PLACEMENT######################
@login_required(login_url='login_view')
def PlaceStudent(request):
    # student=UserAccount.objects.filter(Role_id=2)
    # print("We Gate")
    count=0
    try:
        criteria=request.POST.getlist('criteria')
        if request.method == 'POST': 
            social_male_student=[]
            social_female_student=[]
            natural_male_student=[]
            natural_female_student=[]
            account=UserAccount.objects.all().values()
            for data in account:
                if data['Role_id']==3:
                    stud_id=data['User_id']
                    student=User.objects.get(id=stud_id)
                    b=[]
                    a1=student.Id_no
                    a2=student.FirstName
                    a3=student.LastName
                    a4=student.Gender
                    a5=student.Department
                    a6=student.collage
                    a7=student.stream
                    a8=student.Year_of_Student
                    # #error is here
                    b.append(a1)
                    b.append(a2)
                    b.append(a3)
                    b.append(a4)
                    b.append(a5)
                    b.append(a6)
                    b.append(a7)
                    b.append(a8)
                    #print(b)
                    if b[3]=="Male":
                        # male_student.append(b)
                        if a7=="social":
                            social_male_student.append(b)
                        else:
                            natural_male_student.append(b)
                    else:
                        if a7=="natural":
                            natural_female_student.append(b)
                        else:
                            social_female_student.append(b)
             
            
            if 'collage' in criteria:
                    if 'department' in criteria:
                        if 'batch' in criteria:
                            sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            print("what if")
                            sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            print("Printed")
                            sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            print("We Gate")
                        else:
                            sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[5],x[4],x[1],x[2]))
                            sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[5],x[4],x[1],x[2]))
                            sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[5],x[4],x[1],x[2]))
                            sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[5],x[4],x[1],x[2]))
                    else:  
                        if 'batch' in criteria:
                            sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[5],x[7],x[1],x[2]))
                            sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[5],x[7],x[1],x[2]))
                            sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[5],x[7],x[1],x[2]))
                            sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[5],x[7],x[1],x[2]))
                        else:
                            sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[5],x[1],x[2]))
                            sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[5],x[1],x[2]))
                            sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[5],x[1],x[2]))
                            sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[5],x[1],x[2]))
            else:
                        
                        if 'department' in criteria:
                            
                            if 'batch' in criteria:
                                
                                sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[4],x[7],x[1],x[2]))
                                sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[4],x[7],x[1],x[2]))
                                sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[4],x[7],x[1],x[2]))
                                sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[4],x[7],x[1],x[2]))
                            else:
                                
                                sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[4],x[1],x[2]))
                                sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[4],x[1],x[2]))
                                sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[4],x[1],x[2]))
                                sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[4],x[1],x[2]))
                        else:
                            
                            if 'batch' in criteria:
                                sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[7],x[1],x[2]))
                                sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[7],x[1],x[2]))
                                sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[7],x[1],x[2]))
                                sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[7],x[1],x[2]))
                                
                            else:
                                sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[1],x[2]))
                                sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[1],x[2]))
                                sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[1],x[2]))
                                sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[1],x[2]))
            
            order=['Block','Dorm_name']
            dorm=Dorm.objects.all().order_by(*order).values()
            
            for dorm1 in dorm:
                
                bl=dorm1['Block_id']
                block=Block.objects.get(id=bl)
                if str(block.Block_purpose)=='Males Block'and dorm1['Status']=='Active':
                    #print(sorted_male_social_student)
                   
                    for socmale in sorted_male_social_student: 
                       
                        cnt=Placement.objects.filter(block=block, room=dorm1['Dorm_name']).count()
                        if int(cnt)<int(dorm1['Capacity']):
                            if Placement.objects.filter(Stud_id=socmale[0]).exists():
                                 pass
                            else:
                                #Stud_id,FirstName,LastName,gender,stream,collage,department,batch,block,room
                                place=Placement(Stud_id=socmale[0],FirstName=socmale[1],LastName=socmale[2],gender='Male',stream=socmale[6],collage=socmale[5],department=socmale[4] ,batch=socmale[7] ,block=block,room=dorm1['Dorm_name'])
                                place.save()
                                count=count+1
                                #print(place)
                        else:
                            break 
                    for natmale in sorted_male_natural_student:
                        cnt=Placement.objects.filter(block=block, room=dorm1['Dorm_name']).count()
                        if int(cnt)<int(dorm1['Capacity']):
                            if Placement.objects.filter(Stud_id=natmale[0]).exists():
                                pass
                            else:
                                x=8
                                place=Placement(Stud_id=natmale[0],FirstName=natmale[1],LastName=natmale[2],gender='Male',stream=natmale[6],collage=natmale[5],department=natmale[4],batch=natmale[7] ,block=block,room=dorm1['Dorm_name'])
                                place.save()
                                count=count+1
                                #print(place)
                        else:
                            break
                elif str(block.Block_purpose)=='Females Block'and dorm1['Status']=='Active':
                    # print(sorted_female_social_student)
                    for socfemale in sorted_female_social_student:
                        cnt=Placement.objects.filter(block=block, room=dorm1['Dorm_name']).count()
                        if int(cnt)<int(dorm1['Capacity']):
                            if Placement.objects.filter(Stud_id=socfemale[0]).exists():
                                pass
                            else:
                                place=Placement(Stud_id=socfemale[0],FirstName=socfemale[1],LastName=socfemale[2],gender='Female',stream=natmale[6],collage=socfemale[5],department=socfemale[4],batch=socfemale[7] ,block=block,room=dorm1['Dorm_name'])
                                place.save()
                                count=count+1
                        else:
                            break
                    for natfemale in sorted_female_natural_student:
                        cnt=Placement.objects.filter(block=block, room=dorm1['Dorm_name']).count()
                        if int(cnt)<int(dorm1['Capacity']):
                            if Placement.objects.filter(Stud_id=natfemale[0]).exists():
                                pass
                            else:
                                place=Placement(Stud_id=natfemale[0],FirstName=natfemale[1],LastName=natfemale[2],gender='Female',stream=natfemale[6],collage=natfemale[5],department=natfemale[4] ,batch=natfemale[7] ,block=block,room=dorm1['Dorm_name'])
                                place.save()
                                count=count+1
                        else:
                            break
            if count ==1:
                messages.success(request,'1 Sudent Placed successfully....!!!')    
            elif count==0:
                msg=' All Students Already Placed....!!!'
                messages.info(request,msg)
            else:
                msg=str(count) + ' Sudent Placed successfully....!!!'
                messages.success(request,msg)               
    except:
          messages.error(request,'Empty or Invalid File...!!')
    return render(request, 'StudentDean/uploadstudent.html')

@login_required(login_url='login_view')
def managePlacement(request):
    orderlist=['block','room','Stud_id','FirstName','LastName']
    result=Placement.objects.order_by(*orderlist)
    if request.method =='POST':
        searched=request.POST['searched']
        result=Placement.objects.filter(FirstName__contains=searched)| Placement.objects.filter(LastName__contains=searched)| Placement.objects.filter(department__contains=searched)
        return render(request, "StudentDean/viewPlacementInfo.html",{"Placement":result})
    return render(request,"StudentDean/viewPlacementInfo.html",{"Placement":result})
@login_required(login_url='login_view')
def updateStudent(request,pk):
    #orderlist=['block','room','Stud_id','FirstName','LastName']
    result=Placement.objects.get(id=pk)
    #result1=Placement.objects.order_by(*orderlist)
    form1=AddPlacementForm(request.POST or None,instance=result)
    context = { 'res': result,'form':form1} 
    if form1.is_valid():
        form1.save()
  
        messages.success(request,"Data Updated Succesfully!")
   
    return render(request,'StudentDean/updateStudent.html',context)
@login_required(login_url='login_view')
def delateStudent(request,pk):
    result=Placement.objects.get(id=pk)
    #result1=Dorm.objects.order_by('Block')
    result.delete() 
    
    messages.error(request,"Data Deleted Succesfully!")
    return redirect('managePlacement')

@login_required(login_url='login_view')
def resetPlacement(request):
    if request.method=='POST':
        result=Placement.objects.all()
        #result1=Dorm.objects.order_by('Block')
        if result !=None:
           result.delete() 
        
        messages.success(request,"Data reset Succesfully!")
    return render(request,'StudentDean/resetPlacement.html')
@login_required(login_url='login_view')
def rPlacement(request):
    return redirect('resetPlacement')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('index')
