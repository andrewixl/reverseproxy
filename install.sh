cp startserver.sh /usr/bin/startserver.sh
chmod +x /usr/bin/startserver.sh
cp reverseproxy.service /etc/systemd/system/reverseproxy.service
chmod 644 /etc/systemd/system/reverseproxy.service
systemctl start reverseproxy
systemctl enable reverseproxy