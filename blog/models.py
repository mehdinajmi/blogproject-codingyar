from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    STATUS_CHOICES=(('PUB','Published'),('D','Draft'))
    title=models.CharField(max_length=100)
    text=models.TextField()
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=3)

    def __str__(self):
        return f'{self.title} '

    def get_absolute_url(self):
        return reverse ( 'post_detail_view' , args=[self.id])

