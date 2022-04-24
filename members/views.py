from django.shortcuts import redirect, render
from theblog.models import  Category, Post, Post2, Post3, Post4
from django.urls import reverse_lazy
from django.views import generic
from members.forms import SignUpForm
from django.contrib import messages

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(request):

        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
        
            if password1==password2:
                if user.objects.filter(username=username).exists():
                    messages.info(request, 'Username taken')
                    return redirect('register/')
                elif user.objects.filter(email=email).exist():
                    messages.info(request, 'email taken')
                    return redirect('register/')

                else:


                      user = user.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                      user.save();
                      print('user created')

            else:
                print('passord not matching..')
                return redirect('register')
            return redirect('/')

        else:
            return render(request, 'register.html')

    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context



class UserLoginView(generic.CreateView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    
    def get_context_data(self, *args, **kwargs):
        Cat_menu = Category.objects.all()

        context = super(UserLoginView, self).get_context_data(*args, **kwargs)
        context["Cat_menu"] =  Cat_menu
        return context




