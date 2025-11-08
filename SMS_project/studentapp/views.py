from django.shortcuts import render
from .models import Student, Teacher, Course,Marks,Attendance

def student_list(request):
    students = Student.objects.select_related('course', 'user').all()
    return render(request, 'student_list.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def marks_list(request):
    marks = Marks.objects.all()
    return render(request, 'marks_list.html', {'marks': marks})

def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance': attendance})
