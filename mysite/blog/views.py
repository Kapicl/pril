from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm

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
