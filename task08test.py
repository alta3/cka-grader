import subprocess as sp

def task08(pp=4):
    points = 0
    cmd01 = 'kubectl get pods multicontainer -o jsonpath={.spec.containers[1].image}'
    cmd02 = 'kubectl get pods multicontainer -o jsonpath={.spec.containers[1].image}'
    out01 = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt01 = out01.stdout.read().decode('utf-8')
    txt02 = out02.stdout.read().decode('utf-8')
    for line in [txt01, txt02]:
        if line == "redis":
            points += 2
        if line == "nginx":
            points += 2
    response = {"task": "task08", "points": float(points), "possible": pp, "msg": [(cmd01, txt01), (cmd02, txt02)]}
    return response


if __name__ == "__main__":
    print(task08())
