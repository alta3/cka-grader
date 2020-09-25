import subprocess as sp

def task05(pp=5):
    points = 0
    cmd01 = 'cat /opt/cka/answers/cpu_pod_01.txt'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.strip().startswith("nginx8224-"):
            points += 5
    response = {"task": "task05", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task05())
