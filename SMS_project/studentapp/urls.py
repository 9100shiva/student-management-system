from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('courses/', views.course_list, name='course_list'),
    path('marks/', views.marks_list, name='marks_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
]