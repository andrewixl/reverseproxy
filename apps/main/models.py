# Create your models here.
from __future__ import unicode_literals
from django.db import models
import bcrypt

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

        if results['status'] == True:
            results['config'] = Config.objects.create(name = postData['name'], fqdn = postData['fqdn'], ssl = False, ipAddress = postData['ip'], portNumber = postData['port'],)
        return results

    def createConfig(self, config):
        print (config)
        Config.objects.create(name = config[0], fqdn = config[1], ssl = False, ipAddress = config[2], portNumber = config[3],)


class Config(models.Model):
    name = models.CharField(max_length = 50)
    fqdn = models.CharField(max_length = 50)
    ssl = models.BooleanField(default = False)
    sslexpire = models.DateField(default = "1970-01-01")
    ipAddress = models.CharField(max_length = 50)
    portNumber = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ConfigManager()

    def __str__(self):
        return self.name



class AuthManager(models.Manager):
    def addAuth(self, postData):
        results  = {'status': True, 'errors': [], 'auth': None}
        if len(postData['username']) < 2:
            results['status'] = False
            results['errors'].append('Username too Short')
        if len(postData['password']) < 5  or  postData['password'] != postData['c_password']:
            results['status'] = False
            results['errors'].append('Passwords are not the Same or Do not Meet the Minimum Length Requirement (5)')

        if results['status'] == True:
            p_hash = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
            results['auth'] = Auth.objects.create(status = True, username = postData['username'], password = p_hash)
        return results
    
    def loginVal(self, postData):
        results = {'status': True, 'errors': [], 'auth': None}
        results['auth'] = Auth.objects.filter(username = postData['username'])
        if len(results['auth'] ) <1:
            results['status'] = False
            results['errors'].append('The Username and/or Password is Incorrect')
        else:
            hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), results['auth'][0].password.encode('utf-8'))
            if hashed  != results['auth'][0].password:
                results['status'] = False
                results['errors'].append('The Username and/or Password is Incorrect')
        return results

        
class Auth(models.Model):
    status = models.BooleanField(default=False)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthManager()

    def __str__(self):
        return self.username

