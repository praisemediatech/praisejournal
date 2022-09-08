from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Tag, Comment, Reply, Categories
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from .forms import CommentForm, ReplyForm, SearchFrom
from about.models import About, Interest, Services
from resume.models import Education, Experience
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from contact.forms import ContactForm
from contact.models import ContactInfo
from contact.models import SocialMediaHandles
from hitcount.views import HitCountDetailView
from hitcount.models import HitCount
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from django.contrib import messages


class HomeView(View):
    template_name = 'multiple.html'
    # context_object_name = 'posts'
    # model = Post

    def get(self, request, *args, **kwargs):
        # context = super().get_context_data(*args, **kwargs)
        context = dict()
        context['about'] = About.objects.all()
        context['posts'] = Post.objects.all().order_by('-date')[:3]
        context['interest'] = Interest.objects.all()
        context['experience'] = Experience.objects.all()
        context['education'] = Education.objects.all()
        context['services'] = Services.objects.all()
        context['socialmedia'] = SocialMediaHandles.objects.all()
        context['contactform'] = ContactForm
        context['contact_info'] = ContactInfo.objects.all()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = dict()
        contactform = ContactForm(request.POST or None)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, "Thanks for contacting us. Your message have been sent...")
            return redirect('index')
        else:
            messages.success(request, "Something went wrong. Message not sent.")
        return render(request, self.template_name, context)


class BlogList(ListView):
    context_object_name = 'blog_list'
    template_name = 'blog-list.html'
    paginate_by = 4
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tags'] = Tag.objects.all()
        context['category'] = Categories.objects.all()
        context['recent_news'] = Post.objects.order_by('-date')[:5]
        context['form'] = SearchFrom()
        return context 

    def get_queryset(self):
        queryset = Post.objects.all()
        post_title = self.request.GET.get('title')
        if post_title is not None:
            queryset = queryset.filter(title__contains=post_title)
            if not queryset:
                return Post.objects.all()
        return queryset



class PostDetailView(View):
    template_name = 'single-post.html'
    
    def get(self, request, *args, **kwargs):
        context = dict()
        post = get_object_or_404(Post, slug=kwargs['slug'])
        hit_count = get_hitcount_model().objects.get_for_object(post)
        hits = hit_count.hits
        hitcontext = context['hitcount'] = {'pk': hit_count.pk}
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        if hit_count_response.hit_counted:
            hits = hits + 1
            hitcontext['hit_counted'] = hit_count_response.hit_counted
            hitcontext['hit_message'] = hit_count_response.hit_message
            hitcontext['total_hits'] = hits
        context['comment'] = post.comment_set.filter(verified=True)
        context['comment_count'] = post.comment_set.filter(verified=True).count()
        context['post'] = post
        context['commentform'] = CommentForm()
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        context = dict()
        commentform = CommentForm(request.POST or None)
        post = get_object_or_404(Post, slug=kwargs['slug'])
        new_comment = None
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, "Your comment is being verified...")
            return HttpResponseRedirect(reverse('single_post', args=[post.slug]))
        else:
            context['commentform'] = CommentForm()
            messages.error(request, "Something went wrong. Comment not sent.")
        return context      
        


def commentReply(request, pk, **kwargs):
    template_name = 'reply.html'
    context = dict()
    comment = get_object_or_404(Comment, id=pk)
    context['replyform'] = ReplyForm()
    if request.method == 'POST':
        replyform = ReplyForm(request.POST or None) 
        new_reply = None
        if replyform.is_valid():
            new_reply = replyform.save(commit=False)
            new_reply.comment = comment
            replyform.save()
            return redirect(reverse('single_post', kwargs={'slug':comment.post.slug}))
    return render(request, template_name, context)


class TagList(ListView):
    template_name = 'taglist.html'
    context_object_name = 'taglist'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Categories.objects.all()
        context['tag'] = Tag.objects.all()
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, tag=self.kwargs.get('tag'))
        return Post.objects.filter(tag=tag)


class CatList(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Categories.objects.all()
        context['tag'] = Tag.objects.all()
        return context

    def get_queryset(self):
        category = get_object_or_404(Categories, category=self.kwargs.get('category'))
        return Post.objects.filter(category=category)



