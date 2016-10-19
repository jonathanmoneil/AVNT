## sample flask application
This is a simple flask application deployed into AWS using ansible.


The ansible playbook creates an elb, two instances that will run the flask application behind the elb and an instance that runs mongodb. The application will return a simple `Hello, world!` or can query the DB for a specific value.


##### *The config.yml file should be edited prior to running the playbook.*

```
# Set up config.yml
vi config.yml

# run the playbook 
ansible-playbook playbook.yml

# Grab some coffee
```