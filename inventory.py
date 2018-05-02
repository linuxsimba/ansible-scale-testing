#!/usr/bin/env python

import argparse
import os

try:
    import json
except ImportError:
    import simplejson as json


class DockerInventory(object):

    def __init__(self):
        self.inventory = {}
        self.docker_host = os.environ.get("DOCKER_HOST")
        if not self.docker_host:
            self.docker_host = 'localhost'
        self.read_cli_args()
        self.hostname_base = 'ts'
        self.software_groups = ['app', 'web', 'ntp']
        self.environment_groups = ['dev', 'test', 'prod']
        self.host_count = os.environ.get('HOST_COUNT')
        if not self.host_count:
            self.host_count = 21

        if self.args.host:
            # Implement a -- host option.. Probably not needed but
            # just leave it here
            self.inventory = self.empty_inventory()

        else:
            # if no --list or --host option are specified.  Return an empty inventory
            self.inventory = self.empty_inventory()

        self.create_inventory()
        print(json.dumps(self.inventory))

    def create_inventory(self):

        for _ansible_group in self.software_groups:
            self.inventory[_ansible_group] = {}
            self.inventory[_ansible_group]['hosts'] = []
        for _ansible_group in self.environment_groups:
            self.inventory[_ansible_group] = {}
            self.inventory[_ansible_group]['hosts'] = []
        self.inventory['_meta']['hostvars'] = {}
        hostname_prefix = 'ts'
        software_group_length = len(self.software_groups)
        env_group_length = len(self.environment_groups)
        _env_group_index = 0
        for _count in range(1, self.host_count+1):
            _hostname = "%s%02d" % (hostname_prefix, _count)
            self.inventory['_meta']['hostvars'][_hostname] = {
                'ansible_port': "90%02d" % (_count),
                'ansible_host':  self.docker_host,
                'ntp_master': 'ts01'
            }
            _software_group_index = _count % software_group_length
            _software_group = self.software_groups[_software_group_index]
            self.inventory[_software_group]['hosts'].append(_hostname)
            if ((_count % env_group_length) == 0):
                _env_group_index += 1
                if _env_group_index == (env_group_length):
                    _env_group_index = 0
            _env_group = self.environment_groups[_env_group_index]
            self.inventory[_env_group]['hosts'].append(_hostname)

    def empty_inventory(self):
        return {'_meta': {'host_vars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


if __name__ == '__main__':
    DockerInventory()
