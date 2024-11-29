from django.db import models


class Trip(models.Model):
   # trip_id = models.BigAutoField(blank=True, null=True) change this line to below to make primary key
    trip_id = models.BigAutoField(blank=True, primary_key=True)
    tripduration = models.TextField(blank=True, null=True)  # This field type is a guess.
    starttime = models.TextField(blank=True, null=True)  # This field type is a guess.
    stoptime = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_station_id = models.BigIntegerField(blank=True, null=True)
    start_station_name = models.TextField(blank=True, null=True)
    start_station_latitude = models.FloatField(blank=True, null=True)
    start_station_longitude = models.FloatField(blank=True, null=True)
    end_station_id = models.BigIntegerField(blank=True, null=True)
    end_station_name = models.TextField(blank=True, null=True)
    end_station_latitude = models.FloatField(blank=True, null=True)
    end_station_longitude = models.FloatField(blank=True, null=True)
    bikeid = models.BigIntegerField(blank=True, null=True)
    membership_type = models.TextField(blank=True, null=True)
    usertype = models.TextField(blank=True, null=True)
    birth_year = models.BigIntegerField(blank=True, null=True)
    gender = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TRIP'
