from django.test import TestCase
from todoitem.views import get_index
from django.core.urlresolvers import resolve
from .forms import UserRegistrationForm, UserLoginForm
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.views import login

# Basic Test - addition purely for testing the testing works
class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual( 1 + 2, 3 )
 
    def test_adding_something_isnt_equal(self):
        self.assertNotEqual( 1 + 2, 4 )
        
class UserRegistrationTest(TestCase):
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'djangotestuser1',
            'email': 'djangotestuser@test.com',
            'password1': 'TestPassword999',
            'password2': 'TestPassword999',
        })
        self.assertTrue(form.is_valid())
        
    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Passwords do not match", form.full_clean())
        
    def test_registration_form_fails_with_missing_password(self):
        form = UserRegistrationForm({
            'username': 'djangotestuser2',
            'email': 'djangotestuser@test.com',
            'password1': 'TestPassword999',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Password needs to be entered twice", form.full_clean())