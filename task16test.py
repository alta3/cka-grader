import subprocess as sp

def task16(pp=7):
    points = 0
    cmd01 = 'kubectl logs logger'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.strip().startswith("error: a container name must be specified for pod logger"):
            points += 3
    cmd02 = 'kubectl logs logger -c busylog'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    lines02 = txt02.splitlines()
    lastline = lines02[-1]
    if len(lastline.split()) == 7:
        points += 4
    response = {"task": "task16", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task16())
