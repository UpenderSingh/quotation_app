from django.contrib import admin
from django.urls import path,  include
from uploadcsv.views import ProductImportCSV, ProfileUploadCSV

urlpatterns = [
   path('import_csv/', ProductImportCSV.as_view(), name='import_csv'),
   path('upload_csv/', ProfileUploadCSV.as_view(), name='upload_csv'),
]
