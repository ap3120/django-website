from django.test import TestCase, Client
from django.urls import reverse
from .models import ToDoList, Item
from django.utils import timezone
from django.contrib.auth.models import User

class ToDoListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testpass')
        self.todolist1 = ToDoList.objects.create(name="Test ToDoList 1", date=timezone.now())
        self.todolist2 = ToDoList.objects.create(name="Test ToDoList 2", date=timezone.now())
        self.user.todolist.add(self.todolist1)

    def test_todolist_list_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/view.html')
        self.assertContains(response, self.todolist1.name)
        self.assertContains(response, self.todolist2.name)

    def test_todolist_detail_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('index', args=[self.todolist1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertContains(response, self.todolist1.name)

    def test_todolist_create_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create'), {
            'name': 'Test ToDoList 3',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToDoList.objects.count(), 3)

    """
    def test_todolist_update_view(self):
        response = self.client.post(reverse('todolist-update', args=[self.todolist1.id]), {
            'name': 'Updated Test ToDoList',
        })
        self.assertEqual(response.status_code, 302)
        self.todolist1.refresh_from_db()
        self.assertEqual(self.todolist1.name, 'Updated Test ToDoList')

    def test_todolist_delete_view(self):
        response = self.client.post(reverse('delete', args=[self.todolist1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToDoList.objects.count(), 1)
"""

class ItemTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testpass')
        self.todolist = ToDoList.objects.create(name="Test ToDoList")
        self.user.todolist.add(self.todolist)
        self.item1 = Item.objects.create(text="Test Item 1", toDoList=self.todolist, complete=False)
        self.item2 = Item.objects.create(text="Test Item 2", toDoList=self.todolist, complete=True)

    def test_item_list_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('index', args=[self.todolist.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertContains(response, self.item1.text)
        self.assertContains(response, self.item2.text)

    def test_item_create_view(self):
        response = self.client.post(reverse('index', args=[self.todolist.id]), {
            'text': 'Test Item 3',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Item.objects.count(), 2)

    def test_item_update_view(self):
        response = self.client.post(reverse('index', args=[self.item1.id]), {
            'text': 'Updated Test Item',
            'complete': True,
        })
        self.assertEqual(response.status_code, 200)


