from django.shortcuts import render

# Данные фильмов (можно заменить на базу данных)
MOVIES = [
    {"title": "Интерстеллар", "description": "Космическая эпопея о выживании человечества.", "image": "https://via.placeholder.com/150"},
    {"title": "Начало", "description": "Фильм о проникновении в сознание через сны.", "image": "https://via.placeholder.com/150"},
    {"title": "Матрица", "description": "Культовый фильм о виртуальной реальности.", "image": "https://via.placeholder.com/150"},
]

def movie_list(request):
    return render(request, 'movies.html', {"movies": MOVIES})

