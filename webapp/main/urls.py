from django.urls import path
from .views import (
    createForm,
    list_view, 
    # //Work exercise ,Insert code here    
)

app_name = 'main'
urlpatterns = [
    path('', list_view, name='home-list'),
    path('join-now', createForm)
    # //Work exercise ,Insert code here
]