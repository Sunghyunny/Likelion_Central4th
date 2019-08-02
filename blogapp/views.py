from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog

def index(request):
    return render(request, 'index.html')

def blogMain(request):
    blogs = Blog.objects.all()

    return render(request, 'blogMain.html', {'blogs': blogs})

def createBlog(request):

    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})

    # form = CreateBlog()
    #
    # return render(request, 'createBlog.html', {'form': form})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog_detail': blog_detail})

def edit(request, blog_id):

    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)

        if form.is_valid():
            blog.delete()
            form.save()
            # 지금 이 부분 고쳐야 하는데 경로 설정 임시로 이렇게 해둘게용~~
            # 수정 완료 했습니다~
            return redirect('/blogMain')
        else:
            return redirect('detail')
    else:
        form = CreateBlog(instance=blog)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
        return render(request, 'edit_post.html', context)

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect('/')
