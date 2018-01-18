from django.test import TestCase
from todoitem.views import get_index
from django.core.urlresolvers import resolve

# Create your tests here.
# Check that homepage resolves
class TodoItemPageTest(TestCase):
    def test_todoitem_page_resolves(self):
        todoitem_page = resolve('/')
        self.assertEqual(todoitem_page.func, get_index)