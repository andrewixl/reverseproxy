# Create your models here.
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ConfigManager(models.Manager):
    def createConfig(self, postData):
        results  = {'status': True, 'errors': [], 'config': None}
        if len(postData['name']) < 2:
            results['status'] = False
            results['errors'].append('Config Name too Short')
        if len(postData['fqdn']) < 1:
            results['status'] = False
            results['errors'].append('FQDN is too Short')
        if postData['enable'] == 'True':
            postData['enable'] == True
        else:
            postData['enable'] == False

        if results['status'] == True:
            print ("STATUS INCOMING")
            print (postData['enable'])
            results['config'] = Config.objects.create(enable = postData['enable'], name = postData['name'], fqdn = postData['fqdn'], ipAddress = postData['ip'], portNumber = postData['port'],)
            return results
class Config(models.Model):
    enable = models.BooleanField(default = False)
    name = models.CharField(max_length = 50)
    fqdn = models.CharField(max_length = 50)
    ipAddress = models.CharField(max_length = 50)
    portNumber = models.IntegerField(default = 0)
    objects = ConfigManager()