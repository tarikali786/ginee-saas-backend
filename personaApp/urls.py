from django.urls import path
from . import views
urlpatterns = [
    path('save_data/', views.PersonaAPI.as_view(), name="save_data"),
    path('get_all_data/',views.get,name = 'get_all_data'),
    path('get_selected_data/<pk>/',views.get_data,name = 'get__selected_data'),
    
]