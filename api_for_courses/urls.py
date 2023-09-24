from django.urls import include, path

from rest_framework import routers

from api_for_courses.views import CourseViewSet, CourseInstanceViewSet

router = routers.DefaultRouter()
router.register(r'Course', CourseViewSet)
router.register(r'Course_instance', CourseInstanceViewSet)

urlpatterns = [
   path('', include(router.urls)),
]