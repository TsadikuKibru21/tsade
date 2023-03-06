from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="supervisor"),
    path('assign_block/',views.assign_Block,name='assign_block'),
    path('proctor_info', views.proctor_Info,name="proctor_info"),
    path('logout/',views.logout_View,name='logout'),
]