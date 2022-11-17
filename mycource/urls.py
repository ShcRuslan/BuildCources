from django.urls import path

from mycource import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name= 'courses_list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name= 'course_detail'),
]