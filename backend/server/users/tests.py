from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib import auth

class LogInTest(TestCase):
	""" This class tests login function with correct and wrong data """
	def setUp(self):
		""" This method creates user "user" and client "c" """
		self.user = get_user_model().objects.create_user(username='test', 
														password='12test12', 
														email='test@example.com')
		self.c = Client()


	def tearDown(self):
		""" This method deletes the created user record from the database """
		self.user.delete()


	def test_correct(self):
		""" This method tests user authentication by inputing the correct records"""
		response = self.c.post('/users/login/', {'username': 'test', 
												'password': '12test12'})
		user = auth.get_user(response.wsgi_request)
		self.assertTrue(user.is_authenticated)
		self.assertRedirects(response, '/') #checks the redirection


	def test_wrong_username(self):
		""" tests with wrong username """
		response = self.c.post('/users/login/', {'username': 'wrong', 
												'password': '12test12'})
		user = auth.get_user(response.wsgi_request)
		self.assertFalse(user.is_authenticated)


	def test_wrong_pssword(self):
		""" tests with wrong password """
		response = self.c.post('/users/login/', {'username': 'wrong', 
												'password': '12test12'})
		user = auth.get_user(response.wsgi_request)
		self.assertFalse(user.is_authenticated)