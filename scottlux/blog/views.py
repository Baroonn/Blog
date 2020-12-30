from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

@login_required(login_url='/blog/login')    
def logged(request):
    return render(request, 'blog/loggedin.html', {'username':request.user.username})

@login_required(login_url='/blog/login')    
def tocreate(request):
    return render(request, 'blog/create.html')

@login_required(login_url='/blog/login')
def create(request):
    p = Post(title=request.POST['title'],content=request.POST['content'], date=timezone.now(), user_id_id=request.user.id)
    p.save()
    return HttpResponse("Post successfully created")

@login_required(login_url='/blog/login')    
def show(request):
    return render(request, 'blog/showall.html', {'allposts': Post.objects.filter(user_id_id = request.user.id)})

@login_required(login_url='/blog/login')    
def view(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/view.html',{'p': p})