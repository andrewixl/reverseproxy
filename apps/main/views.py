from django.shortcuts import render,redirect
from .models import Config
from django.contrib import messages

def index(request):
	# Config.objects.all().delete()
	context = {
	'config': Config.objects.all()
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

def createConfig(name, fqdn, ip, port):
	print ("Config Creation Started")
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
	''')
	file.close()