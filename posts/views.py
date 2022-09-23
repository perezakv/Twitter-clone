from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())



    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    #Show
    return render(request, 'posts.html',
                {'posts': posts})

def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post=Post.objects.get(id=post_id)
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)

        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    form=PostForm        


    #Show
    return render(request, 'edit.html',
                {'post': post})

def like(request, id):

    Likedtweet = Post.objects.get(id=id)
    new_value = Likedtweet.like_count +1
    Likedtweet.like_count = new_value
    Likedtweet.save()
    return HttpResponseRedirect('/')