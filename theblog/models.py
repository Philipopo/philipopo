from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')




class Post(models.Model): #the models.py file is used to migrate into the localhost
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/" )
    title_tag = models.CharField(max_length=255, default="sweet16 blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category  = models.CharField(max_length=30, default='relationship')
    snippet  = models.CharField(max_length=250,)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    


    def total_likes(self):
        return self.likes.count()

        
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')



class Post2(models.Model): #the models.py file is used to migrate into the localhost
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/" )
    title_tag = models.CharField(max_length=255, default="sweet16 blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    
    snippet  = models.CharField(max_length=250,)
    likes = models.ManyToManyField(User, related_name = 'blog2_posts')
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post3(models.Model): #the models.py file is used to migrate into the localhost
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/" )
    title_tag = models.CharField(max_length=255, default="sweet16 blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    
    snippet  = models.CharField(max_length=250,)
    likes = models.ManyToManyField(User, related_name = 'blog3_posts')
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post4(models.Model): #the models.py file is used to migrate into the localhost
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/" )
    title_tag = models.CharField(max_length=255, default="sweet16 blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category  = models.CharField(max_length=30, default='relationship')
    
    likes = models.ManyToManyField(User, related_name = 'blog4_posts')
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE, default="sweet16 blog")
    name = models.CharField(max_length=255, default="sweet16 blog")
    body = models.TextField(default="sweet16 blog")
    

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
   
   
    fiverr = models.CharField(max_length=255, null=True, blank=True,)
    facebook = models.CharField(max_length=255, null=True, blank=True,)
    twitter = models.CharField(max_length=255, null=True, blank=True,)
    instagram = models.CharField(max_length=255, null=True, blank=True,)
    
    

    

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')






