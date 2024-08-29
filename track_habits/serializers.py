from rest_framework import serializers

from track_habits.models import Habit
from track_habits.validators import RelatedPleasedHabitValidator, RelatedRewardHabitValidator, \
    PleasedRewardHabitValidator, DurationSecondsValidator, FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedPleasedHabitValidator(field='related_habit'),
            RelatedRewardHabitValidator(field1='related_habit', field2='reward'),
            PleasedRewardHabitValidator(field='is_pleasant'),
            DurationSecondsValidator(field='duration'),
            FrequencyValidator(field='frequency'),
        ]
