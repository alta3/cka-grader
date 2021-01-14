import subprocess as sp

def task17(pp=13):
    points = 0
    cmd01 = 'kubectl get nodes'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.startswith("node-2   Ready"):
            points += 13
    response = {"task": "task17", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task17())
