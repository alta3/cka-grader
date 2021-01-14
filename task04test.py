import subprocess as sp

def task04(pp=7):
    points = 0
    cmd01 = 'ssh master-2 kubectl get nodes'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("master-2"):
            if line.endswith("v1.19.0"):
                points += 7
    response = {"task": "task04", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task04())
