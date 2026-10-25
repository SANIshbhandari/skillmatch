from django.test import TestCase

from accounts.models import User
from profiles.models import CompanyProfile, SeekerProfile
from skills.models import Skill, SkillGroup


class ProfileModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='candidate',
            password='test-password',
        )

    def test_seeker_profile_stores_education_experience_preferences_and_skills(self):
        group = SkillGroup.objects.create(name='Accounting')
        skill = Skill.objects.create(name='Tally', group=group)
        profile = SeekerProfile.objects.create(
            user=self.user,
            education_level=SeekerProfile.EducationLevel.BACHELORS,
            years_experience=2,
            preferences='Remote roles',
        )
        profile.skills.add(skill)

        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.skills.get(), skill)
        self.assertEqual(profile.years_experience, 2)

    def test_company_profile_belongs_to_a_recruiter_user(self):
        recruiter = User.objects.create_user(
            username='recruiter',
            password='test-password',
            role=User.Role.RECRUITER,
        )
        profile = CompanyProfile.objects.create(
            user=recruiter,
            name='Example Company',
            location='Kathmandu',
        )

        self.assertEqual(profile.user.role, User.Role.RECRUITER)
        self.assertEqual(str(profile), 'Example Company')
