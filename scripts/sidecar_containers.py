import pprint as pp
import re
import subprocess as sp

def sidecar_containers():
    # Part 1
    cmd = 'kubectl get pods logger -o jsonpath={.spec.containers[*].name}'
    out = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    c_names = set(txt.split())
    passing01 = True if c_names == {"busylog", "loggingpod"} else False
    
    # Part 2
    cmd02 = 'kubectl logs logger -c busylog'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    lines = txt02.splitlines()
    passing02 = True if len(lines[-1].split()) == 7 else False
    
    # Result
    response = {"task": "Sidecar Containers", 
                "pass": True if passing01 and passing02 else False,
                "msg": "Expected 'busybox' container in 'logger' pod to be running command '/bin/sh -c tail -f /var/log/log01.log'",
                "output": [(cmd, txt), (cmd02, txt02)]}
    return response


if __name__ == "__main__":
    pp.pprint(sidecar_containers())
