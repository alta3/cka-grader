import subprocess as sp

def task02(pp=4):
    points = 0
    cmd01 = 'kubectl get nodes'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.strip().startswith("node-3   Ready,SchedulingDisabled"):
            points += 4
    response = {"task": "task02", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task02())
