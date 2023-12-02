from subprocess import run
import boto3
import json
from datetime import datetime as dt
from os import environ, system

pth = "/data/data/com.termux/files/home/termux-CloudOps/iot/location.json"
cmd = f"termux-location"
bucket_name = environ["BUCKET"]

res = run([cmd], capture_output=True, text=True)
if res.returncode == 0:
    data = json.loads(res.stdout)
    data["timestamp"] = dt.now().isoformat()
    with open (pth, "w") as outfile:
        json.dump(data, outfile, indent=4) 

    system(f"aws s3 cp {pth} {bucket_name}/iot/location/{data['timestamp']}.json")
    print(f"rm {pth}")
    system(f"rm {pth}")

else:
    print("failed")



