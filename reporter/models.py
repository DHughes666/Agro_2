from django.contrib.gis.db import models

# Create your models here.


class Incidence(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __unicode__(self):
        return self.name


class Swamp(models.Model):
    cat = models.FloatField()
    f_codedesc = models.CharField(max_length=80)
    f_code = models.CharField(max_length=80)
    areakm2 = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.f_code


class Airport(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_region = models.BigIntegerField()
    elev = models.FloatField()
    name = models.CharField(max_length=80)
    use = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name
