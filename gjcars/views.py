from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,'gjcars/home.html',context)


class PostListView(ListView):
        model=Post
        template_name='gjcars/home.html'
        context_object_name='posts'
        ordering=['-data_posted']

class PostDetailView(DetailView):
        model=Post
        
        