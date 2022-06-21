import subprocess as sp
import pprint as pp


def pod_replicas():
    cmd01 = 'kubectl get pods'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    dragon_pods = 0
    for line in lines:
        if line.strip().startswith("dragon-"):
            dragon_pods += 1
    passing = True if dragon_pods == 8 else False
    response = {"task": "Pod Replicas", 
                "pass": passing, 
                "msg": f"Expected 8 pods starting with 'dragon-', found {dragon_pods}", 
                "output": (cmd01, txt)}
    return response


if __name__ == "__main__":
    pp.pprint(pod_replicas())
