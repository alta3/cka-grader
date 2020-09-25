import subprocess as sp

def task14(pp=7):
    points = 0
    cmd01 = 'kubectl get svc deppysvc'
    out01 = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt01 = out01.stdout.read().decode('utf-8')
    lines = txt01.splitlines()
    for line in lines:
        if line.startswith("deppysvc"):
            points += 1
            if "NodePort" in line:
                points += 2
            if "80" in line:
                points += 1
            if "TCP" in line:
                points += 1
    cmd02 = 'kubectl describe deploy deppy'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    lines02 = txt02.splitlines()
    for line02 in lines02:
        if line02.strip().startswith("Port:"):
            if "80/TCP" in line02:
                points += 2
    response = {"task": "task14", "points": float(points), "possible": pp, "msg": [(cmd01, txt01), (cmd02, txt02)]}
    return response


if __name__ == "__main__":
    print(task14())
