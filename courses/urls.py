from django.urls import path
from .views import (CourseListCreateView, CourseDetailView, 
                    CourseInstanceListCreateView, CourseInstanceDetailView)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('instances/', CourseInstanceListCreateView.as_view(), name='instance-list-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='instance-list'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceDetailView.as_view(), name='instance-detail'),
]
