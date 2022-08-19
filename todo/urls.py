from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<str:pk>',views.delete,name='delete'),
    ]