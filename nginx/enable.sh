ln -sf $(dirname -- "$(realpath -- $0;)";)/contable /etc/nginx/sites-enabled/contable
sudo systemctl restart nginx.service