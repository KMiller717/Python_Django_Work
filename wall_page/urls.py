from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add-new', views.new_job),	  
    path('create_new_job', views.create_new_job),
]