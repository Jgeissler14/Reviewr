# Reviewr
To create a new app use
python manage.py startapp <App Name>

example: /api/users/
python manage.py startapp users

  
# Updating Ec2 instance
cd on your local machine to directory containing .pem file
ssh -i "djangoApp.pem" ubuntu@ec2-18-209-55-160.compute-1.amazonaws.com
cd ~/django
rm -r Reviewr/
  y
  y
git clone "https://github.com/Jgeissler14/Reviewr.git"
sudo chown :www-data *
sudo service apache2 restart
