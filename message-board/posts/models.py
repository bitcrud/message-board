from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField(max_length=1024)
    title = models.TextField(max_length=256, blank=False, default="-")
    slug = models.CharField(max_length=256, blank=True, default="-", unique=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title[:32]

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = self.title.lower().replace(" ", "-")
            super().save(*args, **kwargs)  # Call the "real" save() method.
        else:
            return
