import subprocess as sp
import requests

def task12(pp=7):
    points = 0
    cmd01 = 'kubectl get ing'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    for line in lines:
        if line.startswith("luau"):
            points += 4
            ip = line.split()[3]
            r = requests.get(f"http://{ip}/aloha")
            if r.text == 'Aloha means "hi"':
                points += 3
    response = {"task": "task12", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task12())
