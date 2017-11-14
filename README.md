# Scale Testing Ansible Tower using Docker Containers


## Create the docker containers

* Install docker-engine

* Build the docker image

```
cd docker
docker build -t linuxsimba/python-and-ssh -t linuxsimba/python-and-ssh:latest .

```

* Create the docker containers

```
ansible-playbook scale-containers.yml
```

It currently builds 36 containers. You can change the numbers
but just remember to use a multiple of 18.  _there is a bug in the inventory.py that forces you to use a multiple of 18_

* Run a test

```
ansible-playbook --private-key=./keys/ansible_test -i inventory.py demo.yml

```
## License

MIT
