from django.urls import path
from votes import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('candidate/<int:candidate_id>/', views.candidate_detail,
        name='detail'),
    path('candidate/create/', views.candidate_create, name='create'),
    path('candidate/update/<int:candidate_id>/', views.candidate_update,
        name='update'),
    path('position/create/', views.position_create, name='pos_create'),
    path('candidate/<int:candidate_id>/vote', views.vote, name='vote')

]
