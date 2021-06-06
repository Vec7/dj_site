from django.shortcuts import render

# Create your views here.
def news_home(req):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(req, 'news/index.html')