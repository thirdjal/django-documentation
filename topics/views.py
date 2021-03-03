from django.views.generic import DetailView, ListView

from .models import Topic


class TopicDetailView(DetailView):
    model = Topic


class TopicListView(ListView):
    model = Topic

    def get_queryset(self):
        return super().get_queryset().filter(parent=None)
