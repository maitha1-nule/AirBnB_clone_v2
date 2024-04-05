#!/usr/bin/env bash
## This script will setup my web_server for the deployment process
## It will make sure nginx is installed if not available then setup
## The server blocks necessary and finaly give ownership where required
sudo apt update -y
sudo apt install nginx -y

data_path="/data/"
web_static_path="/data/web_static/"
releases_path="/data/web_static/releases/"
shared_path="/data/web_static/shared/"
test_release_path="/data/web_static/releases/test/"
index_html_path="/data/web_static/releases/test/index.html"
current_link_path="/data/web_static/current"

sudo mkdir -p "$data_path" "$web_static_path" "$releases_path" "$shared_path" "$test_release_path"

sudo echo -e "Fake content\n" | sudo tee "$index_html_path" > /dev/null

if [ -L "$current_link_path" ]; then
    sudo rm "$current_link_path"
fi

sudo ln -s "$test_release_path" "$current_link_path"
sudo chown -R ubuntu:ubuntu "$data_path"
echo "Web server setup completed successfully."
