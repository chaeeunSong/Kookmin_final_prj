from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy, reverse

from blogapp.forms import BlogCreateForm, BlogUpdateForm
from blogapp.models import Blog


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'blogapp/create.html'

    def form_valid(self, form):
        temp = form.save(commit=False)
        temp.blog_author = self.request.user
        temp.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogapp:detail', kwargs={'pk': self.object.pk})


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blogapp/detail.html'
    context_object_name = 'blogObj'


class BlogReview(generic.ListView):
    model = Blog
    #queryset = Blog.objects.filter(blog_title='하이')
    context_object_name = 'blogs'
    template_name = 'blogapp/new_review.html'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    success_url = reverse_lazy("blogapp:board")
    template_name = 'blogapp/update.html'
    context_object_name = 'blogObj'



class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy("blogapp:board")
    template_name = 'blogapp/delete.html'
    context_object_name = 'blogObj'