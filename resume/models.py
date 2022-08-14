from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField(max_length=20)

    def __str__(self):
        return self.title


class Education(models.Model):
    qualification = models.CharField(max_length=500)
    description = models.TextField()
    date = models.CharField(max_length=20)


    def __str__(self):
        return self.qualification
