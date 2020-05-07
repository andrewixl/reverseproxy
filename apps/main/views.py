from django.shortcuts import render,redirect
from .models import Config, Auth
from django.contrib import messages
import os, datetime
from datetime import time  
from datetime import datetime, date, time, timedelta

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .admin import ConfigResource
from django.http import HttpResponse

import json

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

# Checks if Auth is Active, If Active Checks if User is Logged In
def checkUser(request):
	auth_active = bool(len(Auth.objects.all()))
	# print (auth_active)
	try:
		if auth_active == True:
			if request.session['username']:
				return True
			else:
				return False
		else:
			return True
	except:
		return False
	
# Displays User the Proxy Home Page
def index(request):
	if checkUser(request) == False:
		return redirect('/login')
	context = {
	'config': Config.objects.all(),
	'auth_active': bool(len(Auth.objects.all())),
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
	if (config.ssl == True):
		os.system("sudo certbot delete --cert-name " + config.fqdn)
	os.remove("/etc/nginx/sites-enabled/" + config.name + ".conf")
	os.system("service nginx restart")
	config.delete()
	messages.success(request, 'Config has Been Deleted')
	return redirect('/')


# Creates Nginx Configuration File
def createConfig(name, fqdn, ip, port):
	# print ("Config Creation Started")
	# Ubuntu
	file = open("/etc/nginx/sites-enabled/" + name + ".conf", "w")

	# Windows
	# file = open(name + ".conf", "w")
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

def settings(request):
	if checkUser(request) == False:
		return redirect('/login')
	
	context = {
	'auth_active': bool(len(Auth.objects.all())),
	}
	return render( request, 'main/settings.html', context)

# Enables Authentication
def addAuth(request):
	results = Auth.objects.addAuth(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/settings')
	else:
		# addAuth(request.POST['username'], request.POST['password'], request.POST['c_password'])
		messages.success(request, 'Authentication has Been Enabled')
	return redirect('/settings')

# Disables Authentication
def disableAuth(request):
	Auth.objects.all().delete()
	return redirect('/settings')


def loginAuth(request):
	if checkUser(request) == True:
		return redirect('/')
	return render( request, 'main/login.html')


def loginVal(request):
	results=Auth.objects.loginVal(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/')

	request.session['username'] = results['auth'][0].username
	# print (request.session['username'])
	return redirect('/')

# Logs User out of the Console
def logout(request):
	request.session.flush()
	return redirect('/login')

# Pulls Latest Commit From Github
def runUpdate(request):
	os.system("cd reverseproxy")
	os.system("git pull")
	os.system("pip3 install -r requirements.txt")
	os.system("cd ..")
	os.system("systemctl restart reverseproxy")
	messages.success(request, 'AwB Tech: Reverse Proxy, Has Been Updated to the Latest Version')
	return redirect('/')

# Imports JSON Configuration File
def imports(request):
	if request.method == 'POST':
		configuration = request.FILES['myfile']
		data = json.load(configuration) 
		for i in data: 
			if bool(Config.objects.filter(fqdn=i['fqdn'])):
				print("Exists")
			elif not bool(Config.objects.filter(fqdn=i['fqdn'])):
				print ("Does Not Exist... Adding to Database")
				print (i['name'])
				config = [i['name'], i['fqdn'], i['ipAddress'], int(i['portNumber'])]
				Config.objects.createConfigImport(config)
				print ("Configurations Added")
			else:
				print ("A Fatal Error Has Occurred")
			print(i['fqdn'])
	return redirect('/settings')

# Exports JSON Configuration File
from django.core import serializers
import bcrypt
def exportConfig(request):
	dataset = ConfigResource().export()
	response = HttpResponse(dataset.json, content_type='application/json')
	response['Content-Disposition'] = 'attachment; filename="configurations.json"'
	return response
	return redirect('/settings')