from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return 'Message from' + self.title +"-" + self.author

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'