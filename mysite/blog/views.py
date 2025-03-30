from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Post, Comment
from .forms import UserRegistrationForm, CommentForm

def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserRegistrationForm()
    return render(request, "blog/register.html", {"form": form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    new_comment = None

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "form": form, "new_comment": new_comment})
