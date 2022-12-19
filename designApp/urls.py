from django.urls import path
from . import views

urlpatterns=[
    path('',views.JsonListView.as_view()), 
    path('<int:pk>',views.JsonDetailView.as_view()),    
    path('saveall/', views.SaveAllAPI.as_view()),
    
]
