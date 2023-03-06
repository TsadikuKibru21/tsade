from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name="proctor"),
    path('Student',views.student_info,name="Student"),
]