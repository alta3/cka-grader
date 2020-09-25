import subprocess as sp

def task07(pp=4):
    points = 0
    cmd01 = 'kubectl get pods -o wide | grep noded'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if "node-01" in line:
            points += 4
    response = {"task": "task07", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task07())
