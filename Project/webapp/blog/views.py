from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def get_blog_posts(request):
    template_name = 'blog/blog_posts.html'
    object_list = Post.objects.all()
    paginator = Paginator(object_list,2)
    page_number = request.GET.get('page')
    context = {'object_list':object_list}


    try:
        obj_list = paginator.page(page_number)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)

    return render(request,template_name,context)

#def post_detail_view(request,year,month,day,post):
def post_detail_view(request,id):
    # obj=get_object_or_404(Post,slug=post,
    #                             status='published',
    #                             publish__year=year,
    #                             publish__month=month,
    #                             publish__day=day)
    #print(post)
    #obj = Post.objects.filter(slug__icontains=post,status='published')
    #qs = Post.objects.get(slug__icontains='david-warner-will-have-prepare-himself-for-Eng',status='published')
    obj = Post.objects.get(id=id)

    #context = {'object_list':obj}
    template_name = 'blog/post_detail.html'
    # print(type(qs))
    # print(qs)
    context={'obj':obj}
    return render(request,template_name,context)




#     >>> from django.core.mail import send_mail
# >>> send_mail('Hello shashank','important mail','DURGASOFT',['shashank.ragireddy@gmail.com'])
# 1
# >>> send_mail('Hello shashank','important mail','shashank',['shashank.ragireddy@gmail.com','andal.ragireddy@gmail.cmo'])
# 1
# >>> send_mail('Hello shashank','important mail','shashank',['shashank.ragireddy@gmail.com','andal.ragireddy@gmail.com'])
# 1
# >>>
