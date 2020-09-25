import subprocess as sp

def task09(pp=7):
    points = 0
    cmd01 = 'ssh master-03 kubectl get pods'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("isitback"):    
            points += 4
    cmd02 = 'ssh master-03 ls /opt/'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    lines02 = txt02.splitlines()
    for line02 in lines02:
        li = line02.split()
        if li == ["clusterstate.backup"]:
            points += 3
    response = {"task": "task09", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task09())
