from django.urls import path
from rest_framework.routers import DefaultRouter
from track_habits.views import HabitViewSet, HabitPublicListAPIView, HabitOwnListAPIView

from track_habits.apps import TrackHabitsConfig


app_name = TrackHabitsConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

habit_create = HabitViewSet.as_view({'post': 'create'})
habit_detail = HabitViewSet.as_view({'get': 'retrieve'})
habit_update = HabitViewSet.as_view({'put': 'update', 'patch': 'partial_update'})
user_delete = HabitViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('habit/', HabitOwnListAPIView.as_view(), name='habits_list'),
    path('public/', HabitPublicListAPIView.as_view(), name='public_habits_list'),
    path('habit/create/', habit_create, name='habit_create'),
    path('habit/<int:pk>/', habit_detail, name='habit_retrieve'),
    path('habit/<int:pk>/update/', habit_update, name='habit_update'),
    path('habit/<int:pk>/delete', user_delete, name='habit_destroy'),
] + router.urls
