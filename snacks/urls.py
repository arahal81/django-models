from django.urls import path
from django.urls import path
from .views import SnackListDetailView,SnackListPageView

urlpatterns = [
    
    path('',SnackListPageView.as_view(),name='snack_list'),
    path('<int:pk>/',SnackListDetailView.as_view(),name='snack_detail')]
       