from django.test import TestCase
from django.test import client
from django.contrib.auth.models import User


class IndexWebPageTestCase(TestCase):

    def setUp(self):
        self.c = client.Client()

    def test_index_visiting(self):
        resp = self.c.get('/index/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<h2>Welcome Login111</h2>')
        self.assertTemplateUsed(resp, 'index.html')


class LoginTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('cisco',email='lennon@thebeatles.com',password='cisco')
        self.c = client.Client()

    def test_login_and_logout(self):

        #resp = self.c.get('/accounts/login/')
        #self.assertRedirects(resp, '/index/')

        #Django define
        self.c.login(username='cisco',password='cisco')
        resp = self.c.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'login.html')

        self.c.logout()
        resp = self.c.get('/accounts/logout/')
        self.assertRedirects(resp, '/index/')

    def test_login_and_logout_by_http_protocol(self):

        #resp = self.c.get('/index/')
        #self.assertRedirects(resp, '/accounts/login/?next=/index/')

        resp = self.c.post('/accounts/login/', {'username':'cisco', 'password':'cisco'},follow=True)
        self.assertEqual(resp.redirect_chain,[('http://testserver/index/', 302)])

        resp = self.c.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'login.html')

        self.c.get('/accounts/logout/')
        resp = self.c.get('/accounts/logout/')
        self.assertRedirects(resp, '/index/')

