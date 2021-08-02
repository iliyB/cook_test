from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )

    slug = models.SlugField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name='post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)

    ingredients = RichTextField()
    direction = RichTextField()

    post = models.ForeignKey(
        Post,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Comment(models.Model):
    name = models.CharField(max_length=50)

    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=150)

    message = models.TextField(max_length=350)

    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE
    )
