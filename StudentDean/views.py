from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from account.models import User,UserAccount
from .forms import AddBlockForm,AddDorm
from django.views.generic import DetailView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
import csv, pandas as pd
from .models import *

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib import messages
from .serializers import BlockSerializer,DormSerializer,PlacementSerializer,UserSerializer,SaveFileSerializer,UserUploadSerializer
from rest_framework.renderers import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request, 'Sdeanindex.html')
@login_required(login_url='login_view') 
@csrf_exempt
def BlockAdd(request):
    serializer = BlockSerializer()
    context ={
        'serializer': serializer
    }
    if request.method == 'GET':
        # transformer = Block.objects.all()
        return render(request,'StudentDean/addblock.html',context)
  
    return JsonResponse(serializer.errors, status=400)

from django.contrib import messages

@api_view(['POST'])
@login_required
def blockadd(req):
   
       serializer = BlockSerializer(data=req.data)
       a=req.data
       b=Block.objects.all()
    

       if a['Block_name'] not in str(b):
            if serializer.is_valid():
                serializer.save()
                messages.success(req,'Block added successfuly...!!')
                return redirect('blockadd')
       else:
                    messages.error(req,'Block already existed...!!')
                    return redirect('blockadd')


@csrf_exempt
def add_dorm(request):
    serializer = DormSerializer()
    context ={
        'serializer': serializer
    }
    if request.method == 'GET':
        # transformer = Dorm.objects.all()
        
        return render(request,'StudentDean/add_dorm.html',context)
  
    return JsonResponse(serializer.errors, status=400)



@api_view(['POST'])
def add_dorm1(req):
       serializer = DormSerializer(data=req.data)
       a=req.data
       if a['Dorm_name']=='' or a['Block']=='' or a['Capacity']=='':
          messages.success(req,'all Fields are required...!!')
          return redirect('add_dorm')
       else:
        if Dorm.objects.filter(Dorm_name=a['Dorm_name'] , Block=a['Block'] ).exists() :
            messages.error(req, "This Dorm is already Registerd")
            return redirect('add_dorm')
        
        elif serializer.is_valid():
                serializer.save()
                messages.success(req,'Dorm added successfuly...!!')
                return redirect('add_dorm')
        else:
                messages.success(req,'ERROR...!!')
                return redirect('add_dorm')



def viewblock(request):
    result=Block.objects.order_by('Block_name')
    return render(request ,'StudentDean/viewblock.html',{"Block":result})
def viewdorm(request,pk):
    result=Dorm.objects.filter(Block=pk)
    #result=Dorm.objects.order_by('Block')
    return render(request ,'StudentDean/viewdorm.html',{"Dorm":result })
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
def delatedorm(request,pk):
    result=Dorm.objects.get(id=pk)
    result1=Dorm.objects.order_by('Block')
    result.delete() 
    messages.error(request,"Data Deleted Succesfully!")
    return redirect('viewdorm')
def delateblock(request,pk):
    result=Block.objects.get(id=pk)
    result1=Block.objects.order_by('Block_name')
    result.delete() 
    messages.error(request,"Data Deleted Succesfully!") 
    return redirect('viewblock')
###################USER REGISTRATION###################
@csrf_exempt
def Adduser(request):
    serializer = UserSerializer()
    context ={
        'serializer': serializer
    }
    if request.method == 'GET':
        return render(request,'StudentDean/adduser.html',context)
    return JsonResponse(serializer.errors, status=400)
@api_view(['POST'])
def Adduser1(request):
       
       serializer = UserSerializer(data=request.data)
       a=request.data
       if serializer.is_valid():
            if User.objects.filter(Id_no=a['Id_no']).exists() :
                messages.error(request,'A User With This IDis Already Registered...!!')
                return redirect('adduser')
            serializer.save()
            messages.success(request,'User Registered successfuly...!!')
            return redirect('adduser')
       else:
            messages.error(request,'Insert the Necessary information Data...!!')
            return redirect('adduser')
       



def Import_User(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:      
            myfile = request.FILES['myfile']             
            empexceldata = pd.read_excel(myfile)        
            dbframe = empexceldata
            count=0
            for dbframe in dbframe.itertuples():
                if User.objects.filter(Id_no=dbframe.Id_no).exists():          
                    print("gate")
                    continue
                else:
                    count+=1
                    obj = User.objects.create(Id_no=dbframe.Id_no,FirstName=dbframe.FirstName,LastName=dbframe.LastName, Gender=dbframe.Gender,
                                                    phone_no=dbframe.phone_no,Departmnet=dbframe.Departmnet, Year_of_Student=dbframe.Year_of_Student, Emergency_responder_name=dbframe.Emergency_responder_name,
                                                    Emergency_responder_address=dbframe.Emergency_responder_address, Emergency_responder_phone_no=dbframe.Emergency_responder_phone_no,Employee_id=dbframe.Employee_id )

                    obj.save()
            if count==0:
                messages.warning(request,"All User's are Already Registered...!")
            elif count==1:
                messages.success(request,"One User is Registered Succesfully...!")
            else:
                mess=str(count)+" Users  added successfuly...!!"
                messages.success(request,mess)
                # return render(request, 'StudentDean/uploadusers.html', {'uploaded_file_url': uploaded_file_url}) 
            #
    except:
          messages.error(request,'Empty or Invalid File...!!')
    return render(request, 'StudentDean/uploadusers.html',{})

class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [   
                "Id_no",
                "FirstName",
                "LastName",
                "Gender",
                "phone_no",
                "Department",
                'stream',
                'collage',
                "Year_of_Student",
                "Emergency_responder_name",
                "Emergency_responder_address",
                "Emergency_responder_phone_no",
                "Employee_id",
            ]
        )

        return response
    


##################################
def Import_User1(request):
    # a=User.objects.all()
    # for i in a:
    #      print(i)
    try:
        if request.method == 'POST':      
                       
            count=0
            social_male_student=[]
            natural_male_student=[]
            social_female_student=[]
            natural_female_student=[]

            for data in User.objects.all():
                   
                    
                    if data.Gender=='male':
                         if data.stream=='social':
                              sd=list(data)
                              social_male_student.append(sd)
                         else:
                              sd=list(data)
                              natural_male_student.append(sd)
                    else:
                         if data.stream=='social':
                              sd=list(data)
                              social_female_student.append(sd)
                         else:
                              sd=list(data)
                              natural_female_student.append(sd)
            sorted_male_social_student=sorted(social_male_student,key=lambda x:(x[6],x[7],x[5],x[8],x[1],x[2]))
            sorted_female_social_student=sorted(social_female_student,key=lambda x:(x[6],x[7],x[5],x[8],x[1],x[2]))
            sorted_male_natural_student=sorted(natural_male_student,key=lambda x:(x[6],x[7],x[5],x[8],x[1],x[2]))
            sorted_female_natural_student=sorted(natural_female_student,key=lambda x:(x[6],x[7],x[5],x[8],x[1],x[2]))
            
          
            d_all=Dorm.objects.all().order_by('Block').values()
        
            for dm in d_all:
                    count=0
                    bl=dm['Block_id']
                    block=Block.objects.get(id=bl)
                    for data in sorted_male_social_student:
                        if str(block.Block_purpose)=='Males Block':  
                                if count<int(dm['Capacity']):
                                    
                                    place=Placement(Stud_id=data[0],FirstName=data[1],LastName=data[2],block=block,room=dm['Dorm_name'])
                                    place.save()
                                    count=count+1
                                    
                                    sorted_male_social_student.remove(data)
                                else:
                                    count=0
                                    break
                    
    #  Social Female
            for dm in d_all:
                    count=0
                    bl=dm['Block_id']
                    block=Block.objects.get(id=bl)
                    for data in sorted_female_social_student:
                        if str(block.Block_purpose)=='Females Block':  
                                if count<int(dm['Capacity']):
                                    place=Placement(Stud_id=data[0],FirstName=data[1],LastName=data[2],block=block,room=dm['Dorm_name'])
                                    place.save()
                                    count=count+1
                                    
                                    sorted_female_social_student.remove(data)
                                else:
                                    count=0
                                    break                           
                        

    
            for dm in d_all:
                    count=0
                    bl=dm['Block_id']
                    block=Block.objects.get(id=bl)
                    for data in sorted_male_natural_student:
                        if str(block.Block_purpose)=='Males Block':  
                                if count<int(dm['Capacity']):
                                    
                                    place=Placement(Stud_id=data[0],FirstName=data[1],LastName=data[2],block=block,room=dm['Dorm_name'])
                                    place.save()
                                    count=count+1
                                    
                                    sorted_male_natural_student.remove(data)
                                else:
                                    count=0
                                    break      
            for dm in d_all:
                for data in sorted_female_natural_student:
                        if count<=dm['Capacity']:
                            bl=dm['Block_id']
                            block=Block.objects.get(Block=bl)
                            if block['Block_purpose']=="Females Block":      
                                    place=Placement(data['Stud_id'],dm['id'],data['Stud_FirstName'],data['Stud_LastName'],bl,dm['Dorm_name'])
                                    place.save()
                                    count+=1
                                    sorted_female_natural_student.remove(data)
                            else:
                                count=0
                                break                  
                        
    #   #Natural Female
    #         count=0
    #         for dm in d_all:
    #               for data in sorted_female_natural_student:
    #                   if count<=dm['Capacity']:
    #                     bl=dm['Block_id']
    #                     block=Block.objects.get(Block=bl)
    #                     if block['Block_purpose']==b:      
    #                          place=Placement(data['Stud_id'],dm['id'],data['Stud_FirstName'],data['Stud_LastName'],bl,dm['Dorm_name'])
    #                          place.save()
    #                          count+=1
    #                          sorted_female_natural_student.remove(data)
    #                   else:
    #                        count=0
    #                        break    
            messages.success(request,'Sudent placed successfully....!!!')                
    except:
          messages.error(request,'Empty or Invalid File...!!')
    return render(request, 'StudentDean/uploadstudent.html',{})
