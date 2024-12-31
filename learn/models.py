from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='tag_images/', blank=True, null=True, help_text="Optional image for the tag")

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True)

    def __str__(self):
        return self.title