import subprocess as sp

def task13(pp=4):
    points = 0
    cmd01 = 'cat /opt/cka/answers/bchd.taint'
    cmd02 = 'cat /opt/cka/answers/node-01.taint'
    cmd03 = 'cat /opt/cka/answers/node-02.taint'
    cmd04 = 'cat /opt/cka/answers/node-03.taint'
    out01 = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    out03 = sp.Popen(cmd03, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    out04 = sp.Popen(cmd04, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt01 = out01.stdout.read().decode('utf-8')
    txt02 = out02.stdout.read().decode('utf-8')
    txt03 = out03.stdout.read().decode('utf-8')
    txt04 = out04.stdout.read().decode('utf-8')
    lines = [txt01, txt02, txt03, txt04]
    for line in lines:
        if line.strip() in ['<none>', 'node.kubernetes.io/unschedulable:NoSchedule', 'node-role.kubernetes.io/master:NoSchedule']:
            points += 1
    response = {"task": "task13", "points": float(points), "possible": pp, "msg": [(cmd01, txt01), (cmd02, txt02), (cmd03, txt03), (cmd04, txt04)]}
    return response


if __name__ == "__main__":
    print(task13())
