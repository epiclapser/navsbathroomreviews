from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<slug:slug>/review_detail', views.ReviewDetail.as_view(), name='review_detail'),
]