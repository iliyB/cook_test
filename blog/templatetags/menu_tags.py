from django import template
from blog.models import Category, Post

register = template.Library()

@register.inclusion_tag('blog/include/tags/categories.html')
def get_categories():
    categories = Category.objects.all() #.order_by('name')
    return {'list_category': categories}

@register.inclusion_tag('blog/include/tags/last_posts.html')
def get_last_posts():
    posts = Post.objects.select_related('category').order_by('-id')[:5]
    return {'list_last_post': posts}