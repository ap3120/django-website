from django.test import TestCase, Client
from django.urls import reverse
from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post1 = Post.objects.create(title="Test Post 1", content="This is a test post.")
        self.post2 = Post.objects.create(title="Test Post 2", content="This is another test post.")

    def test_post_list_view(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog-post', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.content)

    def test_post_create_view(self):
        response = self.client.post(reverse('blog-post-create'), {
            'title': 'Test Post 3',
            'content': 'This is a new test post.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 3)

    def test_post_update_view(self):
        response = self.client.post(reverse('blog-post-update', args=[self.post1.id]), {
            'title': 'Updated Test Post',
            'content': 'This is an updated test post.',
        })
        self.assertEqual(response.status_code, 302)
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.title, 'Updated Test Post')
        self.assertEqual(self.post1.content, 'This is an updated test post.')

    def test_post_delete_view(self):
        response = self.client.post(reverse('blog-post-delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)

