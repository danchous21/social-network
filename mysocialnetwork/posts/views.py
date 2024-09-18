from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Сохраняем пост, но не отправляем в базу данных
            post.author = request.user  # Привязываем пост к текущему авторизованному пользователю
            post.save()  # Сохраняем пост в базе данных
            return redirect('home')
    else:
        form = PostForm()  # Если запрос GET, создаём пустую форму
    return render(request, 'posts/create_post.html', {'form': form})
