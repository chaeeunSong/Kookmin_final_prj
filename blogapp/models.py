from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    #on delete = Null ==> 회원탈퇴시에도 블로그는 살아 있어야 하므로
    blog_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blog')
    blog_title = models.CharField(max_length=400, null=True)
    blog_image = models.ImageField(upload_to='blog/', null=False)
    blog_content = models.TextField(null=True)
    blog_person = models.CharField(max_length=400, null=True)

    up_to_date = models.DateTimeField(auto_now_add=True, null=True)