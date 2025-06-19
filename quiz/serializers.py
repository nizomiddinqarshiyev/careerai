from rest_framework import serializers
from .models import Options, Question, Type, Test, Careers, RoadMaps,\
    Body, TestItem, TestResult, Lesson, DoneCourse, Course


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'


class RoadMapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMaps
        fields = '__all__'


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'

class TestItemSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )
    class Meta:
        model = TestItem
        fields = '__all__'

class TestResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class DoneCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoneCourse
        fields = '__all__'

