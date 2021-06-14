from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView

def news_home(req):
    news = Articles.objects.all()
    #news = Articles.objects.order_by('-date')
    return render(req, 'news/index.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm
    #fields = ['title', 'anons', 'full_text', 'date']


def create(req):
    error = ''
    if req.method == 'POST':
        form = ArticlesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error input'

    form = ArticlesForm()

    data = {
        'form': form,
        'title': 'Create',
        'error': error
    }
    return render(req, 'news/create.html', data)