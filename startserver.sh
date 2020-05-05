ip=$(ifconfig ens160 | awk '/inet / {print $2}')
source $HOME/reverseproxy/venv/bin/activate
python3 $HOME/reverseproxy/manage.py runserver $ip:8000
echo $ip
