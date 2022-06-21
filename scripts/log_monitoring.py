import os.path
import pprint as pp
import subprocess as sp


def log_monitoring():
    fn = '/opt/cka/answers/sorted_log.log'
    if os.path.isfile(fn):
        with open(fn) as f:
            txt = f.readlines()
            lines = {line.split(":")[-1].strip() for line in txt}
        correct = {'Unable to locate /var/log/whereditgo.txt', '/var/log/lostagain', '/var/log/hopeless'}
        passing = True if lines == correct else False
        out = f"File {fn} found"
    else:
        out = f"File {fn} was not found"

    response = {"task": "Log Monitoring", "pass": passing, "msg": f"Expected 3 lines in the file: {correct}", "output": (txt, out)}
    return response


if __name__ == "__main__":
    pp.pprint(log_monitoring())
