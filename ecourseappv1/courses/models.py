from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from ckeditor.fields import RichTextField
class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    active = models.BooleanField(default=True)


    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=99, unique=True)
    def __str__(self):
        return self.name

class ItemBase(BaseModel):
    tag = models.ManyToManyField(Tag)

    class Meta:
        abstract = True

class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='course/course')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='lesson/%y/%M')
    course = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Comment(Interaction):
    content = models.CharField(max_length=255)


class Like(Interaction):

    class Meta:
        unique_together = ('user', 'lesson')