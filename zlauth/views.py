from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.models import User

# Create your views here.
User = get_user_model()


@require_http_methods(['GET', 'POST'])
def zllogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                # login
                login(request, user)
                user.is_authenticated
                # Determine whether you need to remember me
                if not remember:
                    # If you do not click Remember Me, then you need to set the expiration time to 0,
                    # that is, it will expire after the browser is closed.
                    request.session.set_expiry(0)
                # If clicked, do nothing and use the default expiration time of 2 weeks.
                return redirect('/')
            else:
                print('Mail or password is incorrect!')
                # form.add_error('email', 'Mail or password is incorrect!')
                # return render(request, 'login.html', context={"form": form})
                return redirect(reverse('zlauth:login'))

def zllogout(request):
    logout(request)
    return redirect('/')

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect(reverse('zlauth:login'))
        else:
            print(form.errors)
            return redirect(reverse('zlauth:register'))
            # return render(request, 'register.html', context={"form": form})


def send_email_captcha(request):
    # ?email=xxx
    email = request.GET.get('email')
    if not email:
        return JsonResponse({"code": 400, "message": 'Email must be passed!'})
    # Generate verification code (take a random 4-digit Arabic number)
    # ['0', '2', '9', '8']
    captcha = "".join(random.sample(string.digits, 4))
    # Store in database
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail("Blog registration verification code", message=f"Your registration verification code is：{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code": 200, "message": "Email verification code sent successfully!"})
