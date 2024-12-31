from django.shortcuts import render
from .models import Tag, Author, BlogPost
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blog_posts'
    ordering = ['-date']

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    context_object_name = 'blog_post'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    context_object_name = 'tag'

def showLearn(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()
    blog_posts = BlogPost.objects.all()
    latest_posts = BlogPost.objects.order_by('-date')[:5]
    featured_posts = BlogPost.objects.order_by('-date')[1   :20]
    context = {
        'tags': tags,
        'authors': authors,
        'blog_posts': blog_posts,
        'latest_posts': latest_posts,
        'featured_posts': featured_posts,
    }
    return render(request,'learn/learn.html', context)

def showLearnBlog(request, blog_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_id)
    context = {
        'blog_post': blog_post,
    }
    return render(request,'learn/blog.html', context)