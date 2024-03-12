from django.db import models

# Create your models here.
# table for storing the data from contact form


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return 'Message from' + self.name +"-" + self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'