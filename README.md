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

* Creating a demo environment with Tower Vagrant (Tested on OS X)

This procedure will create a local testing environment using the Vagrant provided by Ansible.

1. Install:
  * Vagrant

2. Obtain a Tower trial license

3. Provision a vagrant machine using the Tower box

```
$ vagrant init ansible/tower
$ vagrant up --provider virtualbox
$ vagrant ssh
```
4. Paste the `tower-vagrant-inventory.py` script into a custom inventory in Tower
(http://docs.ansible.com/ansible-tower/latest/html/administration/custom_inventory_script.html)

5. Provision your docker containers as above

6. Create a group using the custom inventory script

## License

MIT
