#!/bin/sh

if [ "${AUTHORIZED_KEYS}x" = "x" ]; then
  echo "ERROR: You need to supply AUTHORIZED_KEYS environment variable!"
  exit 1
fi

mkdir -p /root/.ssh/
mkdir /var/run/sshd
echo ${AUTHORIZED_KEYS} > /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

ssh-keygen -A

exec /usr/sbin/sshd -D -e
