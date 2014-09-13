from django.db import models

# Create your models here.
class CableProvider(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
      return self.name
  
class CablePackage(models.Model):
    cable_provider = models.ForeignKey(CableProvider)
    package_name = models.CharField(max_length=255)
    package_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    number_of_channels= models.IntegerField(null=True, blank=True)
    internet_speed = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
      return "Provider: %s, Package: %s" % (self.cable_provider, self.package_name)
    


    
