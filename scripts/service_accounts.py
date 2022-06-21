import pprint as pp
import re
import subprocess as sp


def service_accounts():
    # Part 1
    cmd = 'kubectl describe ClusterRole app-creator'
    out = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    reg01 = "DaemonSets.app\s+\[\]\s+\[\]\s+\[create\]"
    reg02 = "Deployments.app\s+\[\]\s+\[\]\s+\[create\]"
    reg03 = "StatefulSets.app\s+\[\]\s+\[\]\s+\[create\]"
    passing01 = True if re.search(reg01, txt) and re.search(reg02, txt) and re.search(reg03, txt) else False

    # Part 2
    cmd02 = 'kubectl get sa app-dev'
    out02 = sp.Popen(cmd02, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt02 = out02.stdout.read().decode('utf-8')
    passing02 = True if re.search("app-dev", txt02) else False

    # Part 3
    cmd03 = 'kubectl describe ClusterRoleBinding app-crb'
    out03 = sp.Popen(cmd03, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt03 = out03.stdout.read().decode('utf-8')
    reg04 = "Name:\s+app-creator"
    reg05 = "ServiceAccount\s+app-dev"
    passing03 = True if re.search(reg04, txt03) and re.search(reg05, txt03) else False

    response = {"task": "Service Accounts",
                "pass": True if passing01 and passing02 and passing03 else False,
                "msg": "Expected ClusterRole app-creator to allow DaemonSets, Deployments, and StatefulSets to be created. Also, SA app-dev to be created, and bound to the app-creator role",
                "out": [(cmd, txt), (cmd02, txt02), (cmd03, txt03)]}

    return response


if __name__ == "__main__":
    pp.pprint(service_accounts())
