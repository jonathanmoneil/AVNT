## sample flask application
This is a simple flask application deployed into AWS using ansible.


The ansible playbook creates an elb, two instances that will run the flask application behind the elb and an instance that runs mongodb. The application will return a simple `Hello, world!` or can query the DB for a specific value.


##### *The config.yml file should be edited prior to running the playbook.*

```
# Set up environment vars
export AWS_ACCESS_KEY_ID='<access_key>'
export AWS_SECRET_ACCESS_KEY='<secret_key>'
export AWS_REGION='<aws_region>'

# Set up config.yml
vi config.yml

# run the playbook 
ansible-playbook playbook.yml

# Grab some coffee

# Once the servers are provisioned, you can use everything but the DB. 
# In order to set up the DB, IAM roles would need to be created so that 
# the web instances could discover the db instance private_ip.
# Since this is not the case here, we have to manually log into the machines
# and do these final steps to access the db. 

# From the first web machine:
sed -i 's/DB_HOST = /DB_HOST = '<private_ip>'/g' /opt/AVNT/web/conf.py
python /opt/AVNT/web/db.py
systemctl restart flask

# From the 2nd machine only the sed command then the flask restart is required.

```
