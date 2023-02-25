from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from account.models import User,UserAccount
from .forms import *
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
                "Student_or_Not",
            ]
        )

        return response
    


##################################
def Import_User1(request):
    # a=User.objects.all()
    # for i in a:
   # print(1)
    try:
        if request.method == 'POST':      
                       
           # count=0
     
            Social_Male_Student=[]
            Natural_Male_Student=[]
            Social_Female_Student=[]
            Natural_Female_Student=[]

            criteria=request.POST.getlist('student')
            total=0
            if 'collage' in criteria:
                 total+=10
            if 'department' in criteria:
                 total+=5
            if 'batch' in criteria:
                 total+=2
            a=UserAccount.objects.all().values()
           

            
            for data in a:
                   
                   if data['Role_id']==2:
                        temp=[] 
                        stud_id=data['User_id']
                        student=User.objects.get(id=stud_id)
                        temp.append(student.Id_no)
                        temp.append(student.FirstName)
                        temp.append(student.LastName)
                        temp.append(student.Gender)
                        temp.append(student.Department)
                        temp.append(student.collage)
                        temp.append(student.stream)
                        temp.append(student.Year_of_Student)

                        
                        if temp[3]=='M':
                            if temp[6]=='social':
                                 Social_Male_Student.append(temp)
                            else:
                                 Natural_Male_Student.append(temp)
                            # social_male_student.append(data['Id_no'],data['FirstName'],data['LastName'],data['Gender'],data['Department'],data['stream'],data['collage'],data['Year_of_Student'])
                           
                        else:
                            if temp[6]=='social':
                                 Social_Female_Student.append(temp)
                            else:
                                 Natural_Female_Student.append(temp)
                                #natural_male_student.append(data['Id_no'],data['FirstName'],data['LastName'],data['Gender'],data['Department'],data['stream'],data['collage'],data['Year_of_Student'])
            
            Social_Male_Student=student_sort(Social_Male_Student,criteria) 
            Social_Female_Student=student_sort(Social_Female_Student,criteria) 
            Natural_Female_Student=student_sort(Natural_Female_Student,criteria)    
            Natural_Male_Student=student_sort(Natural_Male_Student,criteria)                
                          
            ord=['Block','Dorm_name']
      
            df=Dorm.objects.all().order_by(*ord).values()
            df=list(df)
            dmale=[]
            dfemale=[]
            for d in df:
                 bl=d['Block_id']
                 block=Block.objects.get(id=bl)
                 if str(block.Block_purpose)=='Males Block': 
                      dmale.append(d)
                 else:
                      dfemale.append(d)
                      


####MAlE Placement
                               
####FEMAlE Placement
        
        print(Social_Female_Student)
     
        for dm in dfemale:
              bl=dm['Block_id']
              block=Block.objects.get(id=bl)
             

              if str(dm['Status'])=='Active' and str(block.Status)=='Active' and str(block.Block_purpose=='Males Block'):
                        
                    
                    
                        # print(dm)
                        for socfemale in Social_Female_Student:
                            
                            cnt=Placement.objects.filter(block=block,room=dm['Dorm_name']).count()
                            # Social_Female_Student=student_sort(Social_Female_Student,criteria) 


                            if int(cnt)<int(dm['Capacity']):  
                                       place=Placement(Stud_id=socfemale[0],FirstName=socfemale[1],LastName=socfemale[2],gender='Female',collage=socfemale[5],department=socfemale[4],batch=socfemale[7],block=block,room=dm['Dorm_name'])
                                       if Placement.objects.filter(Stud_id=socfemale[0]).exists():
                                            pass
                                       else:
                                            print(place)
                                            # place.save()
                                            # Social_Female_Student.remove(socfemale)
                        
                            else:
                                break
        print(Natural_Female_Student)                           
        for dm in dfemale:
              bl=dm['Block_id']
              block=Block.objects.get(id=bl)
             

              if str(dm['Status'])=='Active' and str(block.Status)=='Active' and str(block.Block_purpose=='Males Block'):
                        
                        for natfemale in Natural_Female_Student:
                            # sorted_female_social_student=sorted(sorted_female_social_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            
                            cnt=Placement.objects.filter(block=block,room=dm['Dorm_name']).count()
                            # Natural_Female_Student=student_sort(Natural_Female_Student,criteria) 


                            if int(cnt)<int(dm['Capacity']):  
                                       place=Placement(Stud_id=natfemale[0],FirstName=natfemale[1],LastName=natfemale[2],gender='Female',collage=natfemale[5],department=natfemale[4],batch=natfemale[7],block=block,room=dm['Dorm_name'])
                                       if Placement.objects.filter(Stud_id=natfemale[0]).exists():
                                            pass
                                       else:
                                            place.save()
                                            # print(place)
                                            # Natural_Female_Student.remove(natfemale)
                             
                            else:
                                    break
         
        print(Social_Male_Student)         
        for dm in dmale:
              bl=dm['Block_id']
              block=Block.objects.get(id=bl)
             
              if str(dm['Status'])=='Active' and str(block.Status)=='Active' and str(block.Block_purpose=='Females Block'):
                 
                    # print(sorted_male_social_student)
                      
                           # print(dm)
                        for socmale in Social_Male_Student:

                            # sorted_male_social_student=sorted(sorted_male_social_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
      
                            cnt=Placement.objects.filter(block=block,room=dm['Dorm_name']).count()
                            # print(cnt)
                            # Social_Male_Student=student_sort(Social_Male_Student,criteria) 

                            if int(cnt)<int(dm['Capacity']):  
                                        
                                    
                                       place=Placement(Stud_id=socmale[0],FirstName=socmale[1],LastName=socmale[2],gender='Male',collage=socmale[5],department=socmale[4],batch=socmale[7],block=block,room=dm['Dorm_name'])
                                       if Placement.objects.filter(Stud_id=socmale[0]).exists():
                                            pass
                                       else:
                                            place.save()
                                            # print(place)
                                            # Social_Male_Student.remove(socmale)
                                    # male_list_all=sorted(male_list_all,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            else:
                                    
                                    break
        print(Natural_Male_Student)         
        for dm in dmale:
              bl=dm['Block_id']
              block=Block.objects.get(id=bl)
             
              if str(dm['Status'])=='Active' and str(block.Status)=='Active' and str(block.Block_purpose=='Females Block'):
                 
                        for natmale in Natural_Male_Student:

                            # sorted_male_social_student=sorted(sorted_male_social_student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
      
                            cnt=Placement.objects.filter(block=block,room=dm['Dorm_name']).count()
                            # print(cnt)
                            # Natural_Male_Student=student_sort(Natural_Male_Student,criteria) 

                            if int(cnt)<int(dm['Capacity']):  
                                        
                                    
                                       place=Placement(Stud_id=natmale[0],FirstName=natmale[1],LastName=natmale[2],gender='Male',collage=natmale[5],department=natmale[4],batch=natmale[7],block=block,room=dm['Dorm_name'])

                                       if Placement.objects.filter(Stud_id=natmale[0]).exists():
                                            pass
                                       else:
                                            place.save() 
                                            # print(place)
                                            # Natural_Male_Student.remove(natmale)

                                     
                                    
                                    # male_list_all=sorted(male_list_all,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            else:
                                    
                                    break
              
         
        messages.success(request,'Sudent placed successfully....!!!')                
    except:
          messages.error(request,'Empty or Invalid File...!!')
    return render(request, 'StudentDean/Placestudent.html',{})


def student_sort(All_Male_Student,criteria):
     
     if 'collage' in criteria:
                    
                    if 'department' in criteria:
                    
                        if 'batch' in criteria:
                            male_student=sorted(All_Male_Student,key=lambda x:(x[5],x[4],x[7],x[1],x[2]))
                            
                        else:
                            male_student=sorted(All_Male_Student,key=lambda x:(x[5],x[4],x[1],x[2]))
                    else:
                            
                        if 'batch' in criteria:
                            male_student=sorted(All_Male_Student,key=lambda x:(x[5],x[7],x[1],x[2]))
                        else:
                            male_student=sorted(All_Male_Student,key=lambda x:(x[5],x[1],x[2]))
     else:
                        if 'department' in criteria:
                    
                            if 'batch' in criteria:
                                    male_student=sorted(All_Male_Student,key=lambda x:(x[4],x[7],x[1],x[2]))
                            else:
                                male_student=sorted(All_Male_Student,key=lambda x:(x[4],x[1],x[2]))
                        else:
                            
                            if 'batch' in criteria:
                                male_student=sorted(All_Male_Student,key=lambda x:(x[7],x[1],x[2]))
                            else:
                                male_student=sorted(All_Male_Student,key=lambda x:(x[1],x[2]))
     return male_student
          
 



def managePlacement(request):
    orderlist=['block','room','Stud_id','batch','FirstName','LastName']
    result=Placement.objects.order_by(*orderlist)
    return render(request,"StudentDean/viewPlacementInfo.html",{"Placement":result})





def updateStudent(request,pk):
    #orderlist=['block','room','Stud_id','FirstName','LastName']
    result=Placement.objects.get(id=pk)
    #result1=Placement.objects.order_by(*orderlist)
    form1=AddPlacementForm(request.POST or None,instance=result)
    context = { 'res': result,'form':form1} 
    if form1.is_valid():
        form1.save()
  
        messages.success(request,"Data Updated Succesfully!")
   
    return render(request,'StudentDean/updatestudent.html',context)
def delateStudent(request,pk):
    result=Placement.objects.get(id=pk)
    #result1=Dorm.objects.order_by('Block')
    result.delete() 
    
    messages.error(request,"Data Deleted Succesfully!")
    return redirect('managePlacement')


def resetPlacement(request):
    if request.method=='POST':
        result=Placement.objects.all()
        #result1=Dorm.objects.order_by('Block')
        if result !=None:
           result.delete() 
        
        messages.success(request,"Data reset Succesfully!")
    return render(request,'StudentDean/resetPlacement.html')

def rPlacement(request):
    return redirect('resetPlacement')
   