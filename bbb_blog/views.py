
from .models import Category,Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.conf import settings  # 추가
import os
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RemovePostForm
from django.views.generic.edit import FormView


# Create your views here.

def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    
    context1 = {
        "post_latest": post_latest
    }
    return render(req, "index.html", context=context1)

class PostDetailView(generic.DetailView):    
    model = Post    
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # index 함수에서 사용하는 context를 가져와서 합칩니다.
        post_latest = Post.objects.order_by("-createDate")[:3]
        context["post_latest"] = post_latest
        return context




class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','title_image','content','category']
    template_name = "blog/post_form.html"



def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'blog/remove_post.html', {'Post': post})










class RemovePostView(FormView):
    template_name = 'blog/remove_post.html'
    form_class = RemovePostForm

    def get(self, request, *args, **kwargs):
        post_id = kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        form = RemovePostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, *args, **kwargs):
        post_id = kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        form = RemovePostForm(request.POST, instance=post)
        
        if form.is_valid():
            print(os.path.join(settings.MEDIA_ROOT, post.title_image.name))
            os.remove(os.path.join(settings.MEDIA_ROOT, post.title_image.name))
              
            post.delete()
            return redirect('index')  # 삭제 후 리디렉션할 뷰 이름
        else:
            return render(request, self.template_name, {'form': form, 'post': post})










def fashion(req):
    context1 = {
    }
    return render(req, "fashion.html", context=context1)

def about_1(req):
    context1 = {
    }
    return render(req, "about.html", context=context1)

def photo1(req):
    post_latest = Post.objects.order_by("-createDate")[:10]
    context1 = {
        "post_latest": post_latest
    }
    return render(req, "photography.html", context=context1)

def travel1(req):
    post_latest = Post.objects.order_by("-createDate")[:5]
    context1 = {
        "post_latest": post_latest
    }
    return render(req, "travel.html", context=context1)

def contact1(req):
    context1 = {
    }
    return render(req, "contact.html", context=context1)
def single1(req):
    context1 = {
    }
    return render(req, "single.html", context=context1)

# url({%static 'images/bg_1.jpg' %})