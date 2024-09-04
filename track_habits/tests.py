from django.urls import reverse
from rest_framework.test import APITestCase

from track_habits.models import Habit
from users.models import User


class HabitTest(APITestCase):
    """Тестирование модели Habit."""

    def create_user(self, email):
        user = User.objects.create(email=email, )
        user.set_password('test123456')
        return user

    def create_habit(self, owner_habit, place_habit, time_habit, action_habit, is_public):
        return Habit.objects.create(owner_habit=owner_habit, place_habit=place_habit, time_habit=time_habit,
                                    action_habit=action_habit, is_public=is_public)

    def setUp(self):
        self.user = self.create_user('test@test.com')
        self.client.force_authenticate(user=self.user)
        self.habit = self.create_habit(owner_habit=self.user, place_habit='home test', time_habit='09:00',
                                       action_habit='do test', is_public=True)

    def test_habit_create(self):
        url = reverse('track_habits:habit_create')
        data = {
            'place_habit': 'home test',
            'time_habit': '09:00',
            'action_habit': 'do test',
            'is_public': True, }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_habit_retrieve(self):
        url = reverse('track_habits:habit_retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_habit_list(self):
        url = reverse('track_habits:habits_list', args=())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_habit_