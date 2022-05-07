from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm, UserFeedBackForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Ошибка авторизации!')
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешна!')
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_page')

# def feedback(request):
#     if request.method == 'POST':
#         form = UserFeedBackForm(request.POST)
#         if form.is_valid():
#             text = f"""
#             От: {form.cleaned_data['name']}
#             email: {form.cleaned_data['mail']}
#             Текст:
#             {form.cleaned_data['content']}
#             """
#             mail = send_mail(
#                 form.cleaned_data['subject'],
#                 text,
#                 'rusya-mald@yandex.ru',
#                 ['maldybaev.r@yandex.ru',],
#                 fail_silently=False
#             )
#             if mail:
#                 messages.success(request, 'Обращение отправлено!')
#                 return redirect('feedback')
#             else:
#                 messages.error(request, 'Ошибка отправки!')
#         else:
#             messages.error(request, 'Ошибка отправки!')
#     else:
#         form = UserFeedBackForm()

#     return render(request, 'users/feedback.html', {'form': form})