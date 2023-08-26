from django.urls import path, include
from .import views 

urlpatterns =[
   path('Article/', views.PostList.as_view()) 
]