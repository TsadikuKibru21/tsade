from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.adminhome, name='LAdmin'),
    path('useraccount/',views.generateuseraccount,name="useraccount"),
    path('accountmanagment/',views.accountmanagment,name='accountmanagment'),
    path('addrole/',views.AddRole,name="addole"),
    path('grantrole/', views.GrantRole, name="grantrole"),
    path('Aadduser/', views.AddUser,name="Ad_adduser"),
    path('userinfo/',views.userinfo,name="userinfo"),
    path('deleteuser/',views.deleteuser,name="deleteuser"),
    path('logout/',views.logout,name='logout'),
]
