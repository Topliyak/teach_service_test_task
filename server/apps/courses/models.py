from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    lessons = models.ManyToManyField(
        to='Lesson',
        through='LessonInProduct'
    )


class ProductPurchase(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )

    buyer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Lesson(models.Model):
    title = models.TextField()
    video_ref = models.URLField()
    duration_sec = models.IntegerField()


class LessonInProduct(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )
    
    lesson = models.ForeignKey(
        to=Lesson,
        on_delete=models.CASCADE,
    )
    
    lesson_order = models.IntegerField()


class LearningSession(models.Model):
    student = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    lesson = models.ForeignKey(
        to=Lesson,
        on_delete=models.CASCADE,
    )

    finished = models.BooleanField(
        default=False,
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
    )

    finished_at = models.DateTimeField(
        auto_now=True,
    )


class LearningStatus(models.Model):
    name = models.TextField()


class LessonLearning(models.Model):
    student = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE,
    )

    lesson = models.ForeignKey(
        to=Lesson,
        on_delete=models.CASCADE,
    )

    watched_sec = models.IntegerField(
        default=0
    )
    
    status = models.ForeignKey(
        to=LearningStatus,
        on_delete=models.CASCADE,
    )
