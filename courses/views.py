from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# CourseInstance Views
class CourseInstanceListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        queryset = CourseInstance.objects.all()

        if year is not None:
            queryset = queryset.filter(year=year)
        if semester is not None:
            queryset = queryset.filter(semester=semester)

        return queryset

class CourseInstanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        try:
            return CourseInstance.objects.get(year=year, semester=semester, id=course_id)
        except CourseInstance.DoesNotExist:
            raise NotFound(detail="CourseInstance not found.")
