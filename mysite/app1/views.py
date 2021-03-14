from django.shortcuts import render,HttpResponse,redirect
from app1.models import Post,BlogComment

# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    print(allPosts)
    context={'allPosts':allPosts}
    return render(request,'blogHome.html',context)



def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    post.views=post.views + 1
    post.save()
    comments=BlogComment.objects.filter(post=post)
    context={'post':post,'comments':comments}
    return render(request,'blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"your comment is published")
    return redirect("/")


