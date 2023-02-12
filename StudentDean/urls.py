from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="studentdeanhome"),
    #########Add Block
    path('blockadd/',views.BlockAdd,name='blockadd'),
    path('blockadd/blockadd1',views.blockadd,name='blockadd1'),
    ##########Add Dorm
    path('add_dorm/',views.add_dorm,name="add_dorm"),
    path('add_dorm/add_dorm1',views.add_dorm1,name="add_dorm1"),
    ##########
    path('viewblock/', views.viewblock, name="viewblock"),
    path('viewdorm/<int:pk>/',views.viewdorm,name='viewdorm'),
    path('updateblock/<int:pk>/',views.updateblock,name='updateblock'),
    path('updatedorm/<int:pk>/',views.updatedorm,name='updatedorm'),
    path('delatedorm/<int:pk>/',views.delatedorm,name='delatedorm'),
    path('delateblock/<int:pk>/',views.delateblock,name='delateblock'),
    #############User Registration###############3
    path('adduser/',views.Adduser,name='adduser'),
    path('adduser/adduser1',views.Adduser1,name='adduser1'),

    path('Import_User/',views.Import_User,name="Import_User"),
    path('resetPlacement/',views.resetPlacement,name="resetPlacement"),
    path('rPlacement/',views.rPlacement,name="rPlacement"),
    ############
    #path("upload/", views.StudentBulkUploadView.as_view(), name="student_upload"),
    path("download-csv/", views.DownloadCSVViewdownloadcsv.as_view(), name="download_csv"),
    path('Import_User1/',views.Import_User1,name="Import_User1"),
    
    path('managePlacement/',views.managePlacement,name="managePlacement"),
    #path("download-csv1/", views.DownloadCSVViewdownloadcsv1.as_view(), name="download_csv1"),
    path('updateStudent/<int:pk>/',views.updateStudent,name='updateStudent'),
    path('delateStudent/<int:pk>/',views.delateStudent,name='delateStudent'),
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