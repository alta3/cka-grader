import subprocess as sp

def task15(pp=4):
    points = 0
    cmd01 = 'cat /opt/cka/answers/sorted_log.log'
    out = sp.Popen(cmd01, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT, close_fds=True)
    txt = out.stdout.read().decode('utf-8')
    lines = txt.splitlines()
    try:
        for line in lines:
            line = line.split('UTC')
            inner = line[1]
            f = inner.split(': ')[1]
            if f in ['Unable to locate /var/log/whereditgo.txt', '/var/log/lostagain', '/var/log/hopeless']:
                points += 1.33
            if points == 3.99:
                points = 4
    except IndexError as err:
        print(err)
    response = {"task": "task15", "points": float(points), "possible": pp, "msg": [(cmd01, txt)]}
    return response


if __name__ == "__main__":
    print(task15())
