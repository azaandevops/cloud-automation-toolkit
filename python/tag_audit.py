#!/usr/bin/env python3
import boto3

def main():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()
    for r in response["Reservations"]:
        for i in r["Instances"]:
            tags = {x["Key"]: x["Value"] for x in i.get("Tags", [])}
            if "Environment" not in tags or "Owner" not in tags:
                print(f"Missing governance tags: {i['InstanceId']}")

if __name__ == "__main__":
    main()
