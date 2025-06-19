
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Options, Question, Type, Test, Careers, RoadMaps, Body, TestItem, TestResult, Lesson, Course, \
    DoneCourse
from .serializers import OptionsSerializer, QuestionSerializer, TypeSerializer, TestSerializer, CareersSerializer, \
    RoadMapsSerializer, BodySerializer, TestItemSerializer, LessonSerializer, CourseSerializer, DoneCourseSerializer
from rest_framework import generics, viewsets
from rest_framework import permissions
# Create your views here.


class OptionsListView(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class OptionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer   
    permission_classes = [permissions.IsAuthenticated]

class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeListView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestListView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class CareersListView(generics.ListCreateAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    permission_classes = [permissions.IsAuthenticated]


class CareersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoadMapsListView(generics.ListCreateAPIView):
    queryset = RoadMaps.objects.all()
    serializer_class = RoadMapsSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoadMapsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoadMaps.objects.all()
    serializer_class = RoadMapsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BodyListView(generics.ListCreateAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]


class BodyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

class TestItemListView(generics.ListCreateAPIView):
    queryset = TestItem.objects.all()
    serializer_class = TestItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TestItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestItem.objects.all()
    serializer_class = TestItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TestItemCreateView(generics.CreateAPIView):
    queryset = TestItem.objects.all()
    serializer_class = TestItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TestResultView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class LessonAPIView(APIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer
#     def get(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         token = request.GET.get("token")
#         lessons = Lesson.objects.filter()
#         lessons_serializer = serializer(lessons, many=True)
#         return


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Lessons
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# Done Careers
class DoneCareerListCreateAPIView(generics.ListCreateAPIView):
    queryset = DoneCourse.objects.all()
    serializer_class = DoneCourseSerializer

class DoneCareerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoneCourse.objects.all()
    serializer_class = DoneCourseSerializer
