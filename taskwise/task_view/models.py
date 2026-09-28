from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title=models.CharField(max_length=100)

    CATEGORY_OPTIONS=[
        ('HOME','HOME'),
        ('Work','Work'),
        ('PERSONAL','PERSONAL')
    ]
    category=models.CharField(max_length=100,choices=CATEGORY_OPTIONS)

    created_at=models.DateTimeField(auto_now_add=True)

    completed_status=models.BooleanField(max_length=100,default=False)

    PRIORITY_OPTIONS=[
        ('1','LOW'),
        ('2','MEDIUM'),
        ('3','HIGH'),
    ]

    priority=models.CharField(max_length=100,choices=PRIORITY_OPTIONS,default='2')

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
