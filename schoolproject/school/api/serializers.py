from datetime import datetime
from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from classperiod.models import ClassPeriod


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'  


class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, student):
        return f"{student.first_name} {student.last_name}"

    def get_age(self, student):
        if student.date_of_birth:
            today = datetime.now().date()
            age = today.year - student.date_of_birth.year - ((today.month, today.day) < (student.date_of_birth.month, student.date_of_birth.day))
            return age
        return None

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class ClassPeriodSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer() 
    course = CourseSerializer()    
    classroom = ClassroomSerializer()  

    class Meta:
        model = ClassPeriod
        fields = '__all__'
