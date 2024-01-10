from django.shortcuts import render, redirect
from .models import articles
from .forms import articlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})
# Create your views here.


class NewDetailView(DetailView):
    model = articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = articles
    template_name = 'news/create.html'
    
    form_class = articlesForm

class NewsDeleteView(DeleteView):
    model = articles
    success_url = '/news'
    template_name = 'news/blog-delete.html'
    
    


def create(request):
    error = ''
    if request.method == 'POST':
        form = articlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Unavailable form'


    form = articlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)