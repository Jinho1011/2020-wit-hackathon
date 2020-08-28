from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseListView.as_view()),
    path('<str:number>/', CourseDetailView.as_view())
]
