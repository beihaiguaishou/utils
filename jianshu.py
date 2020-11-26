#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os.path as path
import json
import requests
from sys import argv


def upload(token, file: str):
    rsp = requests.get("https://www.jianshu.com/upload_images/token.json?filename=" + path.basename(file),
                       headers={"Cookie": "remember_user_token=" + token, "Accept": "application/json",
                                "User-Agent": "Safari/537.36"})
    assert rsp.status_code == 200
    response_json = json.loads(rsp.content.decode("utf-8"))
    files = {
        "file": (path.basename(file), open(file, "rb")),
        "token": (None, response_json["token"]),
        "key": (None, response_json["key"]),
        "x:protocol": (None, "https")
    }
    rsp = requests.post("https://upload.qiniup.com/", headers={"User-Agent": "Safari/537.36"}, files=files)
    assert rsp.status_code == 200
    print(json.loads(rsp.content.decode("utf-8"))["url"])


if __name__ == "__main__":
    if len(argv) < 2:
        assert False
    for file in argv[2:]:
        upload(argv[1], file)
