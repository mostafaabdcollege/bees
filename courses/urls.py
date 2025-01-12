from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('courses/<int:course_id>/add_exercise/', views.add_exercise, name='add_exercise'),
    path('courses/submit_answer/<int:exercise_id>/', views.submit_answer, name='submit_answer'),
    path('tableau', views.tableau_de_bord, name='tableau_de_bord'),
    path('dashbord', views.dashboard, name='dashboard'),
]
