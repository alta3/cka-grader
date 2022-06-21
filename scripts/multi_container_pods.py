import pprint as pp
import re
import subprocess as sp


def multi_container_pods():
    cmd = 'kubectl get pods multicontainer -o jsonpath={.spec.containers[*].image}'
    out = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    images = set(txt.split())
    passing = True if "redis:7" in images and "nginx:1.19.6" in images else False
    
    response = {"task": "Multi-Container Pods",
                "pass": passing,
                "msg": "Expected to find images 'redis:7' and 'nginx:1.19.6' in pod named 'multicontainer'",
                "output": (cmd, txt)}
    return response


if __name__ == "__main__":
    pp.pprint(multi_container_pods())
