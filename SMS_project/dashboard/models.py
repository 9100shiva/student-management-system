from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField(default="No message yet")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
