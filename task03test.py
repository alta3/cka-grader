import subprocess as sp

def task03(pp=9):
    points = 0
    cmd01 = 'ssh master-1 kubectl get nodes'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.strip().startswith("master-1"):
            points += 7
            if line.strip().endswith("v1.19.0"):
                points += 2
    response = {"task": "task03", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task03())
