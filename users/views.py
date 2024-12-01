from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm

from products.models import Basket

from django.contrib import auth, messages

from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView

from django.contrib.auth.views import LoginView

from django.contrib.messages.views import SuccessMessageMixin

from users.models import User

# Create your views here.

class UserLoginView(LoginView):
    template_name="users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('index   ')

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

class UserRegistrationView(SuccessMessageMixin, CreateView):
    model=User
    form_class = UserRegisterForm
    template_name="users/register.html"
    success_url=reverse_lazy("users:login")
    success_message="Account successfully created."

    def get_context_data(self, **kwargs):
        context=super(UserRegistrationView, self).get_context_data()
        context['title'] = "Store - Registration"
        return context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations. You are registered')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
        baskets = Basket.objects.all()
    context = {
        'title': "Store - Авторизация",
        'form': form,
        'basket': Basket.objects.all(),
    }
    return render(request, 'users/profile.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))