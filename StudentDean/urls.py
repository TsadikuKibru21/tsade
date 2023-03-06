from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="studentdeanhome"),
    #########User Managment#####
    path('addemployee',views.addEmployee,name='addemployee'),
    path('blockadd/',views.BlockAdd,name='blockadd'),
    path('add_dorm/',views.add_dorm,name="add_dorm"),
    path('viewblock/', views.viewblock, name="viewblock"),
    path('viewdorm/<int:pk>/',views.viewdorm,name='viewdorm'),
    path('updateblock/<int:pk>/',views.updateblock,name='updateblock'),
    path('updatedorm/<int:pk>/',views.updatedorm,name='updatedorm'),
    path('delatedorm/<int:pk>/',views.delatedorm,name='delatedorm'),
    path('delateblock/<int:pk>/',views.delateblock,name='delateblock'),
    path('resetPlacement/',views.resetPlacement,name="resetPlacement"),
    path('rPlacement/',views.rPlacement,name="rPlacement"),
    path('Import_User1/',views.PlaceStudent,name="Import_User1"),
    path('managePlacement/',views.managePlacement,name="managePlacement"),
    path('updateStudent/<int:pk>/',views.updateStudent,name='updateStudent'),
    path('delateStudent/<int:pk>/',views.delateStudent,name='delateStudent'),
    path('logout/',views.logout_View,name='logout'),
]


# from django.urls import path

# from .models import Block
# from .serializers import BlockSerializer 
# from .views import BlockView,BlockAdd,blockadd,add_dorm,add_dorm1,home

# urlpatterns = [
#     path('', home, name="studentdeanhome"),
#     path('blockadd/',BlockAdd,name='blockadd'),
#     path('blockadd/blockadd1',blockadd,name='blockadd1'),
#     path('add_dorm/',add_dorm,name='add_dorm'),
#     path('add_dorm/add_dorm1',add_dorm1,name='add_dorm1'),
#     # path('viewblock/',viewblock,name='viewblock'),
# ]
