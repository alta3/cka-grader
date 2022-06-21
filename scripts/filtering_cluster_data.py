import os.path
import pprint as pp
import re
import subprocess as sp


def filtering_cluster_data():
    fn = '/opt/cka/answers/cpu_pod_01.txt'
    if os.path.isfile(fn):
        out = f"{fn} found"
        with open(fn) as f:
            txt = f.read()
            passing = True if re.search("nginx8224-.*", txt) else False
    else:
        passing = False
        out = f"Did not find file {fn}"
        
    response = {"task": "Filtering Cluster Data", 
                "pass": passing,
                "msg": "Expected pod name to begin with 'nginx8224-'",
                "output": out}
    return response


if __name__ == "__main__":
    pp.pprint(filtering_cluster_data())
