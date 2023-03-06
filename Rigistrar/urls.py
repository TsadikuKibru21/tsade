from django.urls import path,include
from .import views
urlpatterns = [
    # path('LAdmin/',include("account.urls"),name="Admin"),
    # path('admin/', admin.site.urls),
    path('',views.index, name="Registrar"),
    path('logout/',views.logout_View,name='logout'),
    path("download-csv/", views.DownloadCSVViewdownloadcsv.as_view(), name="download_csv"),
    path('adduser/',views.Adduser,name='adduser'),
    path('adduser/adduser1',views.Adduser1,name='adduser1'),
    path('Import_User/',views.Import_User,name="Import_User"),
]