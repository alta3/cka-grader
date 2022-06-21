import pprint as pp
import re
import subprocess as sp


def configure_services():
    # Part 1
    cmd01 = 'kubectl get svc deppysvc'
    out01 = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt01 = out01.stdout.read().decode('utf-8')
    regex = "deppysvc.*NodePort.*80:"
    passing01 = True if re.search(regex, txt01) else False

    # Part 2
    cmd02 = 'kubectl describe deploy deppy'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    regex02 = "Port:\s*80\/TCP"
    passing02 = True if re.search(regex02, txt02) else False
    
    # Result
    response = {"task": "Configure Services", 
                "pass": True if passing01 and passing02 else False,
                "msg": f"Expected NodePort svc called 'deppysvc' exposing deployment 'deppy' on port 80",               
                "output": (cmd01, txt01, cmd02, txt02)}
    return response


if __name__ == "__main__":
    pp.pprint(configure_services())
