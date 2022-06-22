#from typing_extensions import Self
from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.user={
            'username':'fatoufall1',
            'email':'fatou@gmail.com',
            'first_name':'Fatou',
            'last_name':'FallSy',
            'password1':'Mmesy29',
            'password2':'Mmesy29'
        }
        self.user_different_password={
            'username':'fatoufall1',
            'email':'fatou@gmail.com',
            'first_name':'Fatou',
            'last_name':'FallSy',
            'password1':'Mmesy29',
            'password2':'Mmesy291'
        }
        self.user_unvalid_email={
            'username':'fatoufall1',
            'email':'fatou.com',
            'first_name':'Fatou',
            'last_name':'FallSy',
            'password1':'Mmesy29',
            'password2':'Mmesy29'
        }
        return super().setUp()

class RegisterTest(BaseTest): 
    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')
    def test_can_register_user(self):
        response=self.client.post(self.register_url, self.user,format='text/html')
        self.assertEqual(response.status_code,200)
    def test_cant_register_user(self):
        response=self.client.post(self.register_url, self.user_different_password,format='text/html')
        self.assertEqual(response.status_code,302)
    def test_cant_register_unvalidemail(self):
        response=self.client.post(self.register_url, self.user_unvalid_email,format='text/html')
        self.assertEqual(response.status_code,200)
  


