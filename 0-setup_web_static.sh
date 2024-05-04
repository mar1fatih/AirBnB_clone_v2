#!/usr/bin/env bash
# set up the web servers for the deployment of web_static
function install() {
	command -v "$1" &> /dev/null
	#shellcheck disable=SC2181
	if [ $? -ne 0 ]; then
		sudo apt-get update -y -qq && \
			sudo apt-get install -y "$1" -qq
		echo -e "\n"
	else
		echo -e "${1} is already installed.\n"
	fi
}
install nginx
sudo ufw allow 'Nginx HTTP'
echo "allowing HTTP"
sudo mkdir /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
echo "completed..."
