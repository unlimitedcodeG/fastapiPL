#!/usr/bin/env python3
# coding:utf-8

# feishu.py
from rich.console import Console

console = Console()
console.print("发射红箭", style="bold red")

import base64
import hashlib
import hmac
from datetime import datetime

import requests

WEBHOOK_URL = (
    "https://open.feishu.cn/open-apis/bot/v2/hook/beb036b7-9947-4dd6-a05e-04222322fdc4"
)
WEBHOOK_SECRET = "pxoSWVzWzlWKg5UpW5qwc"
timestamp = int(datetime.now().timestamp())


def gen_sign(secret):
    # 拼接时间戳以及签名校验
    string_to_sign = "{}\n{}".format(timestamp, secret)

    # 使用 HMAC-SHA256 进行加密
    hmac_code = hmac.new(
        string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()

    # 对结果进行 base64 编码
    sign = base64.b64encode(hmac_code).decode("utf-8")

    return sign


def main():
    sign = gen_sign(WEBHOOK_SECRET)

    params = {
        "timestamp": timestamp,
        "sign": sign,
        "msg_type": "interactive",
    }

    resp = requests.post(WEBHOOK_URL, json=params)
    resp.raise_for_status()
    result = resp.json()
    if result.get("code") and result.get("code") != 0:
        print(f"发送失败：{result['msg']}")
        return


console.print("发射红箭", style="bold red")

if __name__ == "__main__":
    main()
