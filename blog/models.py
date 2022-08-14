from django.db import models
import uuid
from django.template.defaultfilters import slugify 

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.tag

    
class Categories(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    date = models.DateTimeField(auto_now_add=True)
    section_one = models.TextField()
    section_two = models.TextField()
    post_image = models.ImageField(upload_to='', null=True, blank=True)
    quote = models.CharField(max_length=500, null=True, blank=True)
    quote_image = models.ImageField(upload_to='', null=True, blank=True)
    quote_author = models.CharField(max_length=50, default='Praise Media')
    slug = models.SlugField(blank=True, unique=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # id = models.PositiveIntegerField(editable=False, primary_key=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name='Full name')
    email = models.EmailField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    def __str__(self):
        return self.comment



class Reply(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    verified = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'Replies'

    def __str__(self):
        return self.reply