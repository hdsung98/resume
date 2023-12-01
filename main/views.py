from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'services.html')



def memo(request):
  posts = Post.objects.all().order_by('-updated_at')
  paginator = Paginator(posts, 5)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'main/memo.html', {'page_obj': page_obj})

def posting(request, pk):
  post = Post.objects.get(pk=pk)
  return render(request, 'main/posting.html', {'post':post})

# def new_post(request):
#   if request.method == 'POST':
#     if 'mainphoto' in request.FILES:
#       new_article = Post.objects.create(
#         postname=request.POST['postname'],
#         contents=request.POST['contents'],
#         mainphoto=request.FILES['mainphoto'],
#       )
#     else:
#       new_article = Post.objects.create(
#         postname=request.POST['postname'],
#         contents=request.POST['contents'],
#       )
#     return redirect('/memo/')
#   return render(request, 'main/new_post.html')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/memo/')
    else:
        form = PostForm()
    return render(request, 'main/new_post.html', {'form': form})

def edit_post(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return redirect('posting', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'main/edit_post.html', {'form': form})

def delete_post(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    post.delete()
    return redirect('memo')
  return render(request, 'main/delete_post.html', {'post': post})