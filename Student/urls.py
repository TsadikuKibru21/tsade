
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="student"),
    path('viewdorm',views.viewdorm,name='viewdorm'),
    path('logout/',views.logout_View,name='logout'),
]
