from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index') #/polls/
    , path('<int:subject_code_id>/', views.detail, name='detail')
    , path('<int:subject_code_id>/polls_results/', views.results, name='results')
    , path('<int:subject_code_id>/vote/', views.vote, name='vote')
    , path('polls_register/', views.register, name='register')
    , 
]