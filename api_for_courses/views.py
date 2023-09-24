from rest_framework import viewsets

from api_for_courses.serializers import CourseSerializer, CourseInstanceSerializer
from api_for_courses.models import Course, Course_instance


class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer


class CourseInstanceViewSet(viewsets.ModelViewSet):
   queryset = Course_instance.objects.all()
   serializer_class = CourseInstanceSerializer