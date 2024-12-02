# from django.shortcuts import render, HttpResponseRedirect

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm

from products.models import Basket

# from django.contrib.auth.decorators import login_required

# from django.contrib import messages

# from django.contrib import auth

from django.urls import reverse, reverse_lazy

# from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView

from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.views import LoginView

from django.contrib.messages.views import SuccessMessageMixin

from users.models import User

from common.views import TitleMixin

# Create your views here.

class UserLoginView(TitleMixin ,LoginView):
    template_name="users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('index')
    title = "Store - Login"

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#         else:
#             print(form.errors)
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)

class UserRegistrationView(TitleMixin ,SuccessMessageMixin, CreateView):
    model=User
    form_class = UserRegisterForm
    template_name="users/register.html"
    success_url=reverse_lazy("users:login")
    success_message="Account successfully created."
    title = "Store - Registration"

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Congratulations. You are registered')
#             return HttpResponseRedirect(reverse('users:login'))
#         else:
#             print(form.errors)
#     else:
#         form = UserRegisterForm()
#     context = {'form': form}
#     return render(request, 'users/register.html', context)

class UserProfileView(TitleMixin ,UpdateView):
    model=User
    form_class=UserProfileForm
    template_name = "users/profile.html"
    title = "Store - Profile"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context=super(UserProfileView, self).get_context_data()
        context['baskets']=Basket.objects.filter(user=self.object)
        return context

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#         baskets = Basket.objects.all()
#     context = {
#         'title': "Store - Авторизация",
#         'form': form,
#         'basket': Basket.objects.all(),
#     }
#     return render(request, 'users/profile.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))