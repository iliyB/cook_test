from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs.get('slug')).name
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request, 'base.html')
