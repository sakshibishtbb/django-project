from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
   sno=models.AutoField(primary_key=True)
   title=models.CharField(max_length=100)
   content=models.TextField()
   author=models.CharField(max_length=20)
   views=models.IntegerField(default=0)
   slug=models.CharField(max_length=130)
   thumbnail=models.ImageField(upload_to="app1/images",default='')
   timestamp=models.DateTimeField(blank=True)

   def __str__(self):
       return self.title

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField(default="write description")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13]+"by"+self.user,username
    
   
