chmod +x run.sh
export PATH="$PATH:/root/reverseproxy
sudo ln -s /root/reverseproxy/manage.py manage
cp reverseproxy.service /etc/systemd/system/reverseproxy.service
systemctl enable reverseproxy.service
