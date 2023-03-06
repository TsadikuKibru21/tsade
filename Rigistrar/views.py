from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, View
import csv, pandas as pd
from django.contrib import messages
from account.models import User,UserAccount
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import UserSerializer
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def index(request):
    return render(request,'Registrar/index.html')
###################USER REGISTRATION###################
@login_required(login_url='login_view')
@csrf_exempt
def Adduser(request):
    serializer = UserSerializer()
    context ={
        'serializer': serializer
    }
    if request.method == 'GET':
        return render(request,'Registrar/adduser.html',context)
    return JsonResponse(serializer.errors, status=400)
@login_required(login_url='login_view')
@api_view(['POST'])
def Adduser1(request):
       
       serializer = UserSerializer(data=request.data)
       a=request.data
       if serializer.is_valid():
            if User.objects.filter(Id_no=a['Id_no']).exists() :
                messages.error(request,'A User With This ID is Already Registered...!!')
                return redirect('adduser')
            serializer.save()
            messages.success(request,'User Registered successfuly...!!')
            return redirect('adduser')
       else:
            messages.error(request,'Insert the Necessary information Data...!!')
            return redirect('adduser')
@login_required(login_url='login_view')
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
                    
                    print('gate else')
                    obj = User.objects.create(Id_no=dbframe.Id_no,FirstName=dbframe.FirstName,LastName=dbframe.LastName,
                                              Gender=dbframe.Gender,phone_no=dbframe.phone_no,
                                              stream=dbframe.stream,collage=dbframe.collage,
                                              Department=dbframe.Department, 
                                              Year_of_Student=dbframe.Year_of_Student, 
                                              Emergency_responder_name=dbframe.Emergency_responder_name,
                                              Emergency_responder_address=dbframe.Emergency_responder_address, 
                                              Emergency_responder_phone_no=dbframe.Emergency_responder_phone_no)

                    obj.save()
                    count+=1 
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
          msg= 'Error Occured after Inserting '+str(count) +' Data Please Correct Your the table'
          messages.error(request,msg)
         
    return render(request, 'Registrar/uploadusers.html',{})

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
                'stream',
                'collage',
                "Department",
                "Year_of_Student",
                "Emergency_responder_name",
                "Emergency_responder_address",
                "Emergency_responder_phone_no",
            ]
        )

        return response
@cache_control(no_cache=True,must_revalidate=True)
@login_required(login_url='login_view')
def logout_View(request):
    logout(request)
    #del request.session['username']
    return redirect('index')