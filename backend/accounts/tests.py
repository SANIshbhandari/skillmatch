from django.test import TestCase

from accounts.models import User


class UserModelTests(TestCase):
    def test_new_user_defaults_to_seeker_role(self):
        user = User.objects.create_user(
            username='candidate',
            password='test-password',
        )

        self.assertEqual(user.role, User.Role.SEEKER)

    def test_user_role_choices_include_recruiter_and_admin(self):
        role_values = {value for value, _label in User.Role.choices}

        self.assertEqual(role_values, {'seeker', 'recruiter', 'admin'})
