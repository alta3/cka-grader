import pprint as pp
import re
import subprocess as sp

def persistent_volumes():
    # Part 1
    cmd = 'kubectl get pv'
    out = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    regex = "rompv\s+6Gi"
    passing = True if re.search(regex, txt) else False
    
    # Result
    response = {"task": "Persistent Volumes",
                "pass": passing,
                "msg": "Expected pv 'rompv' to exist and have 6Gi storage",
                "output": [(cmd, txt)]}
    return response


if __name__ == "__main__":
    pp.pprint(persistent_volumes())
