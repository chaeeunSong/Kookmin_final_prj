from django.forms import ModelForm
from blogapp.models import Blog


class BlogCreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_person', 'blog_content']


class BlogUpdateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_content']
