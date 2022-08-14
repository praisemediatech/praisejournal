from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    about_content = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.name

class Interest(models.Model):
    interest = models.CharField(max_length=50)
    symbol = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.interest

class Services(models.Model):
    service = models.CharField(max_length=100, null=True, blank=True)
    service_description = models.TextField()
    symbol = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


