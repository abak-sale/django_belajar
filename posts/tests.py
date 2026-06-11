from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Membuat data tiruan di database khusus testing
        cls.post = Post.objects.create(text="Ini tes pesan")

    def test_model_content(self):
        # Menguji apakah isi database sesuai
        self.assertEqual(self.post.text, "Ini tes pesan")

    def test_url_exists_at_correct_location(self):
        # Menguji apakah URL '/' bisa diakses (Status 200)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        # Menguji apakah template yang dipakai sudah benar
        response = self.client.get(reverse("posts"))
        self.assertTemplateUsed(response, "posts.html")