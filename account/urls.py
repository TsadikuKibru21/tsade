

from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.adminhome, name='LAdmin'),
    path('useraccount/',views.generateuseraccount,name="useraccount"),
    path('accountmanagment/',views.accountmanagment,name='accountmanagment'),
    
    path('Aadduser/', views.AddUser,name="Ad_adduser"),
    path('userinfo/',views.userinfo,name="userinfo"),
    path('deleteuser/',views.deleteuser,name="deleteuser"),
    path('grantrole/', views.GrantRole, name="grantrole"),
    path('updaterole/<int:pk>/',views.updaterole,name='updaterole'),
    #path('updateblock/<int:pk>/',views.updateblock,name='updateblock'),
    path('logout/',views.logout_View,name='logout'),
]