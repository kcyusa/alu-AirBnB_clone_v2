#!/bin/bash
#web static development

sudo apt-get update

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
  sudo apt-get install -y nginx
fi

# Create the required directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Hello, Nginx!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create (or recreate) the symbolic link
if [ -L /data/web_static/current ]; then
  sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
nginx_conf="/etc/nginx/sites-available/default"
sudo sed -i "/server_name _;/a \\
    location /hbnb_static {\\n\\
        alias /data/web_static/current/;\\n\\
    }" $nginx_conf

# Restart Nginx to apply the changes
sudo service nginx restart

