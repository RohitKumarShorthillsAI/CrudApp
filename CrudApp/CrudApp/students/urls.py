from django.contrib import admin
from django.urls import path
from students import views 
from students.views import StudentAPIView

urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='student-api'),
]