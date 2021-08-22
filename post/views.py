from django.shortcuts import render, HttpResponse, redirect
from post.models import Post

# Create your views here.
def post(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    
    return render(request, 'post/post.html', context )
    #return HttpResponse('This is courseshome. We wiil keep all the courses here')
