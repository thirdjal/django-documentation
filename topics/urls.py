from django.urls import path

from .views import TopicDetailView, TopicListView

app_name = "topics"
urlpatterns = [
    path("", TopicListView.as_view(), name="list"),
    path("<int:pk>/", TopicDetailView.as_view(), name="detail"),
]
