from django.db import models

class sms4(models.Model):
    ROLE_CHOICES = [('student', 'Student'), ('teacher', 'Teacher')]

    FullName = models.CharField(max_length=200, null=False)
    Email = models.EmailField(unique=True, null=False)
    Username = models.CharField(max_length=200, null=False, unique=True)
    Password = models.CharField(max_length=200, null=False)
    Role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=False)

    def __str__(self):
        return self.Username
