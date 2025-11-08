from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment, Attendance, Marks, Notice

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(Notice)
