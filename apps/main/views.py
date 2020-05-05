from django.shortcuts import render,redirect
from .models import Config
from django.contrib import messages
import os, datetime
from datetime import time  
from datetime import datetime, date, time, timedelta

def index(request):
	# Config.objects.all().delete()
	context = {
	'config': Config.objects.all(),
	# 'datetime' : datetime.date.today()
	}
	return render( request, 'main/index.html', context)

def addConfig(request):
	results = Config.objects.createConfig(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/')
	else:
		createConfig(request.POST['name'], request.POST['fqdn'], request.POST['ip'], request.POST['port'])
		messages.success(request, 'New Config has Been Created')
	return redirect('/')

def removeConfig(request, id):
	config = Config.objects.get(id=id)
	os.remove("/etc/nginx/sites-enabled/" + config.name + ".conf")
	os.system("service nginx restart")
	config.delete()
	messages.success(request, 'Config has Been Deleted')
	return redirect('/')


# Creates Nginx Configuration File
def createConfig(name, fqdn, ip, port):
	print ("Config Creation Started")
	# Ubuntu
	# file = open("/etc/nginx/sites-enabled/" + name + ".conf", "w")

	# Windows
	file = open(name + ".conf", "w")
	file.write(
'''server {
    server_name ''' + fqdn + ''';
 
    location / {
            proxy_pass http://''' + ip + ''':''' + port + ''';
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}
}
	''')
	file.close()
	os.system("service nginx restart")

def addSSL(request, id):
	config = Config.objects.get(id=id)
	os.system("certbot --nginx --nginx -d " + config.fqdn + " --non-interactive --agree-tos --register-unsafely-without-email --redirect")
	os.system("service nginx restart")
	config.ssl = True
	config.sslexpire = date.today() + timedelta(days=90)
	config.save()
	messages.success(request, 'SSL has Been Added to the ' + config.name + ' Config')
	return redirect('/')

def renewSSL(request, id):
	# config = Config.objects.get(id=id)
	# os.system("certbot --nginx --nginx -d " + config.fqdn + " --non-interactive --agree-tos --register-unsafely-without-email --redirect")
	# os.system("service nginx restart")
	# config.ssl = True
	# config.save()
	# messages.success(request, 'SSL has Been Added to the ' + config.name + ' Config')
	return redirect('/')