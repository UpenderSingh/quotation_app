from django.contrib import admin
from django.urls import path
from .views import ItemSearchView
urlpatterns = [
    path('item_search/', ItemSearchView.as_view(), name='item_search'),
]
