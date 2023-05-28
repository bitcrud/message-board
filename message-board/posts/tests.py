from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            text="hello world", title="Hello World Post", slug="hello-world-post"
        )

    def test_model_content(self):
        self.assertEqual(self.post.text, "hello world")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "hello world")
