sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev
sudo pip2 install virtualenv
mkdir ~/spartan
cd ~/spartan
virtualenv spartan
source spartan/bin/activate
pip2 install django==1.9.5 django-widget-tweaks==1.4.1 django-recaptcha==1.0.5 gunicorn

