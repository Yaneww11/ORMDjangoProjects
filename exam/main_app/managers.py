from django.db import models
from django.db.models import Count


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return (self.prefetch_related('missions')
                .annotate(mission_count=Count('missions'))
                .order_by('-mission_count', 'phone_number'))

    def get_astronaut_top_commanders(self):
        return (self.prefetch_related('missions')
                .annotate(commanded_mission_count=Count('commanders'))
                .order_by('-commanded_mission_count', 'phone_number')
                )

