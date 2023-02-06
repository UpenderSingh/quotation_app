from django.contrib import admin
from django.urls import path,  include
from user_account import views
urlpatterns = [
    path("", views.TemplateView.as_view(template_name = "user_account/home.html"), name = "home"),
    path('admin/', admin.site.urls),
    path('api/user/', include('user_account.urls')),
    path('api/uploader/', include('uploadcsv.urls')),
]
