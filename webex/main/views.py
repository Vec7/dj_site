from django.shortcuts import render


# Create your views here.
def index(req):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(req, 'main/index.html', data)

def about(req):
    return render(req, 'main/about.html')