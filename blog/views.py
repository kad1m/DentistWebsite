from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView, View
from .forms import CommentForm, PostShareViaEmail
from django.shortcuts import redirect
from django.db.models import Count
from .models import Post, Comment


# Create your views here.


def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an mails

        send_mail(
            message_name,  # subject
            message,  # message
            settings.EMAIL_HOST_USER,  # from email
            [message_email]  # to email
        )

        return render(request, "contact.html", {'message_name': message_name})
    else:
        return render(request, "contact.html")


def pricing(request):
    return render(request, 'pricing.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


class ArticleView(ListView):
    paginate_by = 10
    model = Post
    context_object_name = 'posts'
    template_name = 'article_list.html'



class ArticleDetailView(DetailView):
    model = Post
    slug_field = 'slug'
    template_name = 'article_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context

        context = super().get_context_data(**kwargs)
        context['similar_posts'] = self.get_object().tags.similar_objects()[:3]
        context['share_form'] = PostShareViaEmail()
        context['comment_form'] = CommentForm()
        return context


class ArticleByTagView(ListView):
    template_name = 'article_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().filter(tags__slug=self.kwargs['slug'])


class CommentView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return redirect('article_detail', slug)


class SharePostView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, status='draft')

        name = request.POST['name']
        to = request.POST['to']
        post_url = request.build_absolute_uri(post.get_absolute_url())
        subject = '{} ({}) recommends you reading "{}"'.format(name, to, post.title)
        message = 'Read "{}" at {}\n\n{}\'s '.format(post.title, post_url, name)
        send_mail(subject, message, settings.EMAIL_HOST_USER, [to])

        return redirect('article_detail', slug)


def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        message = '<html><head></head><body>'\
                  '<strong>Name:</strong> {your_name}<br>' \
                  '<strong>Phone number:</strong> {your_phone}<br>' \
                  '<strong>Email:</strong> {your_email}<br>' \
                  '<strong>Address:</strong> {your_address}<br><' \
                  'strong>Scheldule:</strong> {your_scheldule}<br>' \
                  '<strong>Date:</strong> {your_date} <br>' \
                  '<strong>Message:</strong> {your_message}<br></body></html>'.format(
            your_name=your_name,
            your_phone=your_phone,
            your_email=your_email,
            your_address=your_address,
            your_scheldule=your_scheldule,
            your_date=your_date,
            your_message=your_message
        )
        print(message)

        send_mail(
            'Dear ' + your_name +', your appointment is ready',  # subject
            message,  # message
            settings.EMAIL_HOST_USER,  # from email
            [your_email]  # to email
        )
        return render(request, "apointment.html", {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_scheldule': your_scheldule,
            'your_date': your_date,
            'your_message': your_message
        })
    else:
        return render(request, "home.html")


