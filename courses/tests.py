from django.test import TestCase
from .models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        Course.objects.create(title="Intro to AI", course_code="CS 101", description="AI basics")

    def test_course
