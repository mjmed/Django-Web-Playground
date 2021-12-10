from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test3', 'test3@test.com', 'test1234')
    
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test3').exists()
        self.assertEqual(exists, True)