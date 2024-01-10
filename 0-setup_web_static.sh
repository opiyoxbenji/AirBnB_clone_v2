#!/usr/bin/env bash
#hat sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /usr/share/nginx/html;
	index index.html;
	add_header X-Served-By $HOSTNAME;
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html
	}
	location /redirect_me {
		return 301 https://www.youtube.com;
	}
	error_page 404 /custom_404.html;
	location = /custom_404.html{
		internal;
	}
}" > /etc/nginx/sites-available/default
sudo service nginx restart
