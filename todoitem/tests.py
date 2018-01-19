from django.test import TestCase
from .forms import TodoItemForm
from todoitem.views import get_index, add_item
from django.core.urlresolvers import resolve

# Create your tests here.
# Check that homepage resolves
class TodoItemPageTest(TestCase):
    def test_todoitem_page_resolves(self):
        todoitem_page = resolve('/')
        self.assertEqual(todoitem_page.func, get_index)
        
# class TestToDoItemForm(TestCase):
#     def test_createtodoitem(self):
#         form = TodoItemForm({"name":"Test create to do item", "description":"Test Description", "status":"Done"})
#         self.assertTrue(form.is_valid())