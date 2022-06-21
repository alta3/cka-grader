import pprint as pp
import re
import subprocess as sp

def pvc_and_storage():
    # Part 1
    cmd01 = 'kubectl get pvc rwopvc'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    regex01 = "rwopvc\s+Bound\s+rwopv\s+5Gi\s+RWO"
    passing01 = True if re.search(regex01, txt) else False
    
    # Part 2
    cmd02 = 'kubectl describe pod rwopod'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    regex02 = "ClaimName:\s+rwopvc"
    passing02 = True if re.search(regex02, txt02) else False
    
    # Result 
    response = {"task": "PVC and Storage", 
            "pass": True if passing01 and passing02 else False,
            "msg": "Expected pvc rwopvc to be Bound to rwopv in RWO mode, and rwopod have PVC of rwopvc",
            "output": [(cmd01, txt, cmd02, txt02)]}
    return response


if __name__ == "__main__":
    pp.pprint(pvc_and_storage())
