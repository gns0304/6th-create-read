from django.db import models

# Create your models here.

# 글제목, 언제 생성되었는지, 언제 업데이트가 되었는지, 블로그 글


class Blog(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title