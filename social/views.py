from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from social import models
from django.db.models import Q

class Wall(LoginRequiredMixin,ListView):
    #queryset = models.Post.objects.all()
    context_object_name = "posts"
    # template_name = "social/posts.html"
    login_url = 'auth/login'

    def get_queryset(self):
        return models.Post.objects.filter(
            (Q(user__friend1=self.request.user.pk) | Q(user__friend2=self.request.user.pk)) &
            ~Q(user=self.request.user)
        )

class Home(LoginRequiredMixin,ListView):
    #queryset = models.Post.objects.all()
    # template_name = "social/posts.html"
    login_url = 'auth/login'

    def get_queryset(self):
        return models.Post.objects.filter(
            Q(user=self.request.user)
        )