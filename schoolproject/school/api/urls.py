from django.urls import path
from .views import ClassPeriodDetailView, CourseDetailView, StudentDetailView, StudentListView, TeacherDetailView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassroomListView
from .views import ClassPeriodListView
from .views import TimetableListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
    path('courses/', CourseListView.as_view(), name='course_list_view'),
    path('classrooms/', ClassroomListView.as_view(), name='classroom_list_view'),
    path('classperiods/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("classes/<int:id>/", ClassPeriodDetailView.as_view(), name="class_detail_view"),
    path("teachers/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    path("courses/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    path("class_period/<int:id>/", ClassPeriodDetailView.as_view(), name="class_period_detail_view"),
    path('timetables/', TimetableListView.as_view(), name='timetable_list_view'),
]