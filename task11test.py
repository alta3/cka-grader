import subprocess as sp

def task11(pp=6):
    points = 0
    cmd01 = 'kubectl get pvc'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.strip().startswith("rwopvc"):
            points += 2
            if "RWO" in line.split():
                points += 1
            if "Bound" in line.split():
                points += 1
    cmd02 = 'kubectl get pod rwopod'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    lines02 = txt02.splitlines()
    for line02 in lines02:
        if line02.strip().startswith("rwopod"):
            points += 2
    response = {"task": "task11", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task11())
