from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_activate)
        self.assertFalse(user.is_staff)
        self.asserFalse(user.is_superuser)
        try:
            self.assertIsnNone(suer.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.crate_user(email='', password='foo')
    
    def test_create_supueruser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        
