from django.contrib.auth import get_user_model
from django.http import request, response
from django.test import TestCase, Client, RequestFactory
from django.urls import resolve

from myhash.models import Myhash
from myhash.views import top, hash_new

UserModel = get_user_model()

class TopPageViewTest(TestCase):
    def test_top_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Myhash", status_code=200)
    
    def test_top_uses_expected_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "myhash/top.html")

class CreateHashTest(TestCase):
    def test_should_resolve_hash_new(self):
        found = resolve("/myhash/new/")
        self.assertEqual(hash_new, found.func)

class TopPageRenderMyhashTest(TestCase):
    def  setUp(self):
        self.user=UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.myhash=Myhash.objects.create(
            msg="test_msg1",
            hsh="test_hash1",
        )
    
    def test_should_return_myash_msg(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.myhash.msg)

#    def test_should_return_username(self):
#        request = RequestFactory().get("/")
#        request.user = self.user
#        response = top(request)
#        self.assertContains(response, self.user.username)

class CreateMyhashTest(TestCase):
    def setUp(self):
        self.user=UserModel.objects.create(
            username="test_user1",
            email="test1@example.com",
            password="abccret",
        )
        self.client.force_login(self.user)
    
    def test_render_creation_form(self):
        response = self.client.get("/myhash/new/")
        self.assertContains(response, "register", status_code=200)
    
    def test_create_myhash(self):
        data = {'msg':'msg1', 'hsh':'myhash'}
        self.client.post("/myhash/new/", data)
        myhash = Myhash.objects.get(msg='msg1')
        self.assertEqual('myhash', myhash.hsh)