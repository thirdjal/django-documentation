from django.db import models
from django.urls import reverse_lazy


class Topic(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subtopics",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    example = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.pk})
