from django.shortcuts import render
from studentapp.models import Student, Teacher, Course
from dashboard.models import Announcement

def dashboard(request):
    # Fetch all students and teachers with related course details
    students = Student.objects.select_related('course', 'user').all()  # keep 'course' for students
    teachers = Teacher.objects.prefetch_related('courses').all()  # fixed line
    courses = Course.objects.all()
    announcements = Announcement.objects.all().order_by('-date_posted')[:5]

    # Counts
    total_students = students.count()
    total_teachers = teachers.count()
    total_courses = courses.count()

    context = {
        'students': students,
        'teachers': teachers,
        'courses': courses,
        'announcements': announcements,
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_courses': total_courses,
    }

    return render(request, 'dashboard.html', context)
