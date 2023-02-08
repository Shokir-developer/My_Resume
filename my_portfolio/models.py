from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class MySkills(models.Model):
    skill_name = models.CharField(max_length=20)
    skill_degree = models.IntegerField()

    def __str__(self):
        return self.skill_name


class MyPortfolio(models.Model):
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=128)
    image = models.ImageField(upload_to='portfolio/')
    type = models.CharField(max_length=4)

    def __str__(self):
        return self.description


class SendModel(models.Model):
    fish = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.fish


class Blogs(models.Model):
    CATEGORY = (
        ('Web dasturlash', 'Web dasturlash'),
        ('Python', 'Python'),
        ('Deployment', 'Deployment')
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=28, choices=CATEGORY)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title
