from django.urls import path
from django.views.generic import TemplateView

from blogapp.views import BlogCreateView, BlogDetailView, BlogReview, BlogUpdateView, BlogDeleteView

app_name = 'blogapp'




urlpatterns = [
    #path('review', TemplateView.as_view(template_name="blogapp/review.html"), name='review'),
    path('board', BlogReview.as_view(template_name="blogapp/review.html"), name='board'),
    path('review', BlogReview.as_view(template_name="blogapp/new_review.html"), name='review'),
    path('create', BlogCreateView.as_view(template_name="blogapp/create.html"), name='create'),
    path('detail/<int:pk>', BlogDetailView.as_view(template_name="blogapp/detail.html"), name='detail'),

    # 추가
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]