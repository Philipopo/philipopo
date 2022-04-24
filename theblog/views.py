from django.shortcuts import render
from .models import Post, Post2, Post3, Post4, Category, Comment, Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, request

# Create your views here.
def error_404(request,exception):
    return render(request, '404.html')


def  home(request):

    Postdisplay = Post.objects.all().order_by('-id')
    Post2display = Post2.objects.all().order_by('-id')
    Post3display = Post3.objects.all().order_by('-id')
    Post4display = Post4.objects.all().order_by('-id')
    Post5display = Profile.objects.all().order_by('-id')
    Cat_menu = Category.objects.all()
    Postcount = Post.objects.all().count()

    

    return render(request,"home.html", {"Post":Postdisplay,"Post2":Post2display ,"Post3":Post3display ,"Post4":Post4display, "Profile":Post5display, "Cat_menu":Cat_menu, "Postcount":Postcount })  


def  blog(request):

    Postdisplay = Post.objects.all().order_by('-id')
    Post2display = Post2.objects.all().order_by('-id')
    Post3display = Post3.objects.all().order_by('-id')
    Post4display = Post4.objects.all().order_by('-id')
    Post5display = Profile.objects.all().order_by('-id')
    Cat_menu = Category.objects.all()
    Postcount = Post.objects.all().count()


    

    return render(request,"blog.html", {"Post":Postdisplay,"Post2":Post2display ,"Post3":Post3display ,"Post4":Post4display, "Profile":Post5display,"Cat_menu":Cat_menu })

class AddPostView(CreateView):
    model = Post
    
    template_name = 'add_post.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context


class AddPost2View(CreateView):
    model = Post2
    
    template_name = 'add_post2.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(AddPost2View, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context
  


class AddPost3View(CreateView):
    model = Post3
    
    template_name = 'add_post3.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(AddPost3View, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context



class AddPost4View(CreateView):
    model = Post4
    
    template_name = 'add_post4.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(AddPost4View, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context

    
class DeletePost2View(DeleteView):
    model = Post2
    template_name = 'delete_post2.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(DeletePost2View, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context






class DeletePost3View(DeleteView):
    model = Post3
    template_name = 'delete_post3.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(DeletePost3View, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context



class DeletePost4View(DeleteView):
    model = Post4
    template_name = 'delete_post4.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(DeletePost4View, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context





def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    Cart_menu = Category.objects.all()
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'Cat_menu':category_posts , "Cart_menu":Cart_menu})
    
class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(DeleteCategoryView, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context



def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'Cat_menu':cat_menu_list})  








class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()
   
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
       
       
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
       
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True






 
        context["Cat_menu"] =  Cat_menu
      
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class Article2DetailView(DetailView):
    model = Post2
    template_name = 'article2_detail.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()
   
        context = super(Article2DetailView, self).get_context_data(*args, **kwargs)
       
       
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
       
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True






 
        context["Cat_menu"] =  Cat_menu
      
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class Article3DetailView(DetailView):
    model = Post3
    template_name = 'article3_detail.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()
   
        context = super(Article3DetailView, self).get_context_data(*args, **kwargs)
       
       
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
       
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True






 
        context["Cat_menu"] =  Cat_menu
      
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context





class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)







        
           
        
        





def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)] ))





