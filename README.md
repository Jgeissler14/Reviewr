# Reviewr
To create a new app use 
python manage.py startapp <App Name> 

example: /api/users/ 
python manage.py startapp users 

  
# Updating Ec2 instance 
cd on your local machine to directory containing .pem file <br>
ssh -i "djangoApp.pem" ubuntu@ec2-18-209-55-160.compute-1.amazonaws.com <br>
cd ~/django <br>
rm -r Reviewr/ <br>
  y <br>
  y <br>
git clone "https://github.com/Jgeissler14/Reviewr.git" <br>
sudo chown :www-data * <br>
sudo service apache2 restart <br>
