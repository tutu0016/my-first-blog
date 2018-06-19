from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register/',views.register, name='register'),
    path('index/', views.index, name='index'),
#    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
#    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
]