import os.path
import pprint as pp


def taints_and_tolerations():
    hosts = ["controller", "node-1"]
    taints = {"controller": "<none>", "node-1": "<none>"}
    passes = []
    for host in hosts:
        fn = f"/opt/cka/answers/{host}.taint"
        if os.path.isfile(fn):
            out = f"File {fn} found"
            with open(fn) as f:
                txt = f.read()
                passing = True if txt.strip() == taints[host] else False
                passes.append(passing)
        else:
            out = f"File {fn} was not found"
            passes.append(False)
    result = {"task": "Taints and Tolerations", 
              "pass": True if passes[0] and passes[1] else False,
              "msg": f"Expected the following taints: {taints}",
              "output": out}
    return result


if __name__ == "__main__":
    pp.pprint(taints_and_tolerations())
