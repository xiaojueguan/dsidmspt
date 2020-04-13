import os
import json
import uuid
import copy


TEMPLATE_DIR = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))),), 'schema')

def get_files_in_dir(src):
    files = os.listdir(src)
    return files

def load_file_as_dict(path):
    result = None
    with open(path, 'r') as fd:
        result = json.loads(fd.read())
    return result

def url_join(a, b):
    return os.path.join(a, b)

def generat_uuid():
    return uuid.uuid1()

def deepcopy(tar):
    return copy.deepcopy(tar)

def update_key_value_in_dict(key_name, value, tar_dict):
    key_updated = False
    for key, value in tar_dict.items():
        if key == key_name:
            tar_dict[key] = value
        else:
            if type(value) is dict:
                update_key_value_in_dict(key_name, value, value)
            else:
                key_updated = True
                return key_updated
test = {
    "event_type":"instance.create.end",
    "payload":{
        "nova_object.data":{
            "architecture":"x86_64",
            "availability_zone": "nova",
            "block_devices":[],
            "created_at":"2012-10-29T13:42:11Z",
            "display_name":"some-server",
            "display_description":"some-server",
            "fault":None,
            "host":"compute",
            "host_name":"some-server",
            "ip_addresses": [{
                "nova_object.name": "IpPayload",
                "nova_object.namespace": "nova",
                "nova_object.version": "1.0",
                "nova_object.data": {
                    "mac": "fa:16:3e:4c:2c:30",
                    "address": "192.168.1.3",
                    "port_uuid": "ce531f90-199f-48c0-816c-13e38010b442",
                    "meta": {},
                    "version": 4,
                    "label": "private-network",
                    "device_name": "tapce531f90-19"
                }
            }],
            "key_name": "my-key",
            "keypairs": [{
                "nova_object.name": "KeypairPayload",
                "nova_object.namespace": "nova",
                "nova_object.version": "1.0",
                "nova_object.data": {
                    "user_id": "fake",
                    "name": "my-key",
                    "fingerprint": "1e:2c:9b:56:79:4b:45:77:f9:ca:7a:98:2c:b0:d5:3c",
                    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGgB4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0lRE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYcpSxsIbECHw== Generated-by-Nova",
                    "type": "ssh"
                }
            }],
            "kernel_id":"",
            "launched_at":"2012-10-29T13:42:11Z",
            "image_uuid": "155d900f-4e14-4e4c-a73d-069cbf4541e6",
            "metadata":{},
            "locked":False,
            "node":"fake-mini",
            "os_type":None,
            "progress":0,
            "ramdisk_id":"",
            "reservation_id":"r-npxv0e40",
            "state":"active",
            "task_state":None,
            "power_state":"running",
            "tags":["tag"],
            "tenant_id":"6f70656e737461636b20342065766572",
            "terminated_at":None,
            "auto_disk_config":"MANUAL",
            "flavor": {
                "nova_object.name": "FlavorPayload",
                "nova_object.data": {
                    "flavorid": "a22d5517-147c-4147-a0d1-e698df5cd4e3",
                    "name": "test_flavor",
                    "root_gb": 1,
                    "vcpus": 1,
                    "ephemeral_gb": 0,
                    "memory_mb": 512,
                    "disabled": False,
                    "rxtx_factor": 1.0,
                    "extra_specs": {
                        "hw:watchdog_action": "disabled"
                    },
                    "projects": None,
                    "swap": 0,
                    "is_public": True,
                    "vcpu_weight": 0
                },
                "nova_object.version": "1.3",
                "nova_object.namespace": "nova"
            },
            "updated_at": "2012-10-29T13:42:11Z",
            "user_id":"fake",
            "uuid":"178b0921-8f85-4257-88b6-2e743b5a975c"
        },
        "nova_object.name":"InstanceCreatePayload",
        "nova_object.namespace":"nova",
        "nova_object.version":"1.7"
    },
    "priority":"INFO",
    "publisher_id":"nova-compute:compute"
}

result = update_key_value_in_dict('user_id', 'a22d5517-147c-4147-a0d1-e698df5cd4e3', test)
print(test)
print(result)