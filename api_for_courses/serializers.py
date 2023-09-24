from rest_framework import serializers

from api_for_courses.models import Course, Course_instance

class CourseSerializer(serializers.ModelSerializer):
   class Meta:
       model = Course
       fields = ('Title', 'Course_code', 'Description')


class CourseInstanceSerializer(serializers.ModelSerializer):
   class Meta:
       model = Course_instance
       fields = ('Year', 'Semester', 'Course_id')