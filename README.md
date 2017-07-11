# Scale Testing Ansible Tower using Docker Containers


## Create the docker containers

* Install docker-engine

* Build the docker image

```
cd docker
docker build -t linuxsimba/debian-python-and-ssh -t linuxsimba/debian-python-and-ssh:latest .

```

* Create the docker containers

```
ansible-playbook scale_containers.yml
```

It currently builds 18 containers. You can change the numbers
but just remember to use a multiple of 18.  _there is a bug in the inventory.py that forces you to use a multiple of 18_

* Change permissions on ./keys/ansible_test

```
chmod 600 ./keys/ansible_test
```

* Run a test

```
ansible-playbook --private-key=./keys/ansible_test -i inventory.py demo.yml

```
## License

MIT
