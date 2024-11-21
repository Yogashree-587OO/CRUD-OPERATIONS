from django.urls import path 

from App.views import Student1
from App.views import Getview 
from App.views import Deleteview
from App.views import PutView
from App.views import PatchView


urlpatterns = [
    path('post/', Student1.as_view()), 
    path('get/',Getview.as_view()),# Ensure this path
    path('delete/', Deleteview.as_view()), 
    path('put/', PutView.as_view()), 
    path('pathch/', PatchView.as_view()),
    
]



