import pprint as pp
import re
import subprocess as sp

def pod_scheduling():
    cmd = 'kubectl get pods noded -o wide'
    out = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    regex = "noded.+Running.+node-1"
    passing = True if re.search(regex, txt) else False
            
    response = {"task": "Pod Scheduling", 
                "pass": passing, 
                "msg": "Expected the 'noded' pod to be running on 'node-1'",
                "output": (cmd, txt)}
    return response


if __name__ == "__main__":
    pp.pprint(pod_scheduling())
