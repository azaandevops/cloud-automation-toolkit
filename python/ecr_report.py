#!/usr/bin/env python3
import boto3

def main():
    ecr = boto3.client("ecr")
    for repo in ecr.describe_repositories()["repositories"]:
        details = ecr.describe_images(repositoryName=repo["repositoryName"])["imageDetails"]
        print(f"{repo['repositoryName']}: {len(details)} image manifests")

if __name__ == "__main__":
    main()
