from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Обработка данных формы и загружаемых файлов
        if form.is_valid():
            user = form.save()  # Сохранение нового пользователя
            login(request, user)  # Автоматический вход пользователя в систему
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()  # Если запрос GET, создаётся пустая форма
    return render(request, 'users/register.html', {'form': form})  # Отображение шаблона с формой
