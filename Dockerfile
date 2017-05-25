FROM python:2.7-wheezy
MAINTAINER linuxsimba

# Merge Python-alpine and polandj/smounives-ssh
# To create a docker that behaves like a Ansible SSH capable node
RUN apt-get update && apt-get -y upgrade && apt-get -y install openssh-server
RUN echo "PasswordAuthentication no" > /etc/ssh/sshd_config
RUN echo "Protocol 2" >> /etc/ssh/sshd_config
RUN echo "Subsystem sftp /usr/lib/openssh/sftp-server" >> /etc/ssh/sshd_config

ADD run.sh /run.sh
RUN chmod +x /*.sh

EXPOSE 22
CMD ["sh", "/run.sh"]
