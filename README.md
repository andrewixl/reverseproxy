# AwB Tech Reverse Proxy (NGINX)
The reverse proxy is a nginx gui with SSL support through Let's Encrypt Certbot to manage your local webservers and allow them to be externally routable from outside your network through IP Forwarding.

## Requirements
 - Ubuntu Server 18.04 (SSL Not Supported on Ubuntu Server 20.04)
 - 10 GB Storage Space
 - 1 GB RAM

## Installation

```bash
sudo -i
apt-get update && apt-get upgrade -y
apt-get install python3-pip python3-dev nginx fail2ban git python3-certbot-nginx -y
apt-get update
pip3 install virtualenv
git clone https://github.com/andrewixl/reverseproxy.git

cd reverseproxy
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo ufw allow 8000
bash install.sh
```

## Usage
Reverse Proxy GUI is Accessable at SERVER_IP:8000

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
