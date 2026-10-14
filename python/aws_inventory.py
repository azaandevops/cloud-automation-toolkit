#!/usr/bin/env python3
import json
import boto3

def main():
    ec2 = boto3.client("ec2")
    instances = []
    for reservation in ec2.describe_instances()["Reservations"]:
        for i in reservation["Instances"]:
            instances.append({
                "id": i["InstanceId"],
                "state": i["State"]["Name"],
                "type": i["InstanceType"],
                "private_ip": i.get("PrivateIpAddress"),
                "tags": {t["Key"]: t["Value"] for t in i.get("Tags", [])},
            })
    print(json.dumps(instances, indent=2))

if __name__ == "__main__":
    main()
