from django.urls import path
from .views import OptionsListView, OptionsDetailView, QuestionListView, QuestionDetailView, TypeListView, \
    TypeDetailView, TestListView, TestDetailView, CareersListView, CareersDetailView, RoadMapsListView, \
    RoadMapsDetailView, BodyListView, BodyDetailView, TestItemDetailView, TestItemCreateView, TestItemListView, \
    TestResultView, CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, LessonListCreateAPIView, \
    LessonRetrieveUpdateDestroyAPIView, DoneCareerListCreateAPIView, DoneCareerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('options/', OptionsListView.as_view(), name='options-list'),
    path('questions/', QuestionListView.as_view(), name='questions-list'),
    path('types/', TypeListView.as_view(), name='types-list'),
    path('tests/', TestListView.as_view(), name='tests-list'),
    path('careers/', CareersListView.as_view(), name='careers-list'),
    path('roadmaps/', RoadMapsListView.as_view(), name='roadmaps-list'),
    path('bodies/', BodyListView.as_view(), name='bodies-list'),


    path('options/<int:pk>/', OptionsDetailView.as_view(), name='options-detail'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='questions-detail'),
    path('types/<int:pk>/', TypeDetailView.as_view(), name='types-detail'),
    path('tests/<int:pk>/', TestDetailView.as_view(), name='tests-detail'),
    path('careers/<int:pk>/', CareersDetailView.as_view(), name='careers-detail'),
    path('roadmaps/<int:pk>/', RoadMapsDetailView.as_view(), name='roadmaps-detail'),
    path('bodies/<int:pk>/', BodyDetailView.as_view(), name='bodies-detail'),
    path('test-items/', TestItemListView.as_view(), name='test-item'),
    path('add-test-item/', TestItemCreateView.as_view(), name='test-item'),
    path('test-item-detail/<int:pk>/', TestItemDetailView.as_view(), name='test-item'),
    path('test-result/<int:pk>/', TestResultView.as_view(), name='test-result'),

    path('api/courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail'),

    # Lessons
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-detail'),

    # Done Careers
    path('done-courses/', DoneCareerListCreateAPIView.as_view(), name='done-course-list-create'),
    path('done-courses/<int:pk>/', DoneCareerRetrieveUpdateDestroyAPIView.as_view(), name='done-course-detail'),
]