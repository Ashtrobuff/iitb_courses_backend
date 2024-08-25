'''##from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstance
        fields = '__all__'
'''
from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description','course_code']  # Adjust fields as needed

class CourseInstanceSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_title', 'year', 'semester']  # Include course_title

##
from rest_framework import generics
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
        queryset = CourseInstance.objects.all()
        year = self.request.query_params.get('year')
        semester = self.request.query_params.get('semester')
        
        if year:
            queryset = queryset.filter(year=year)
        if semester:
            queryset = queryset.filter(semester=semester)
        
        return queryset

class CourseInstanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        course_id = self.kwargs['course_id']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.get(course_id=course_id, year=year, semester=semester)
