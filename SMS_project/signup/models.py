from django.db import models
# Create your models here.
class sms4(models.Model):#sms4 table name in mysql database
    ROLE_CHOICES=[('student','Student'),('teacher','Teacher')]
    FullName=models.CharField(max_length=200,null=False)
    Email=models.CharField(max_length=200,null=False,unique=True)
    Username=models.CharField(max_length=200,null=False)
    Password=models.CharField(max_length=200,null=False)
    Role=models.CharField(max_length=200,choices=ROLE_CHOICES,default='student')

    