from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Contact Information'

    def __str__(self):
        return self.email


class SocialMediaHandles(models.Model):
    social_media = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    link = models.CharField(max_length=500, default='#')

    def __str__(self):
        return self.social_media