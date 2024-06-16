import json
import requests
from requests_toolbelt import MultipartEncoder


class Send_feishu_msg:
    # 应用凭证，获取方式查看上面的步骤
    app_id = "cli_xxxxxxxxxxxxxxx"
    app_secret = "nEkQ8A2x13_xxxxxxxxxxx"
    # 机器人webhook
    chatGPT_url = "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxxxx"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
    }
    json_data = {
        "config": {"wide_screen_mode": True},
        "header": {
            "template": "green",
            "title": {"tag": "plain_text", "content": "📢📢📢xxxxxxxxxxx📢📢📢"},
        },
        "elements": [
            {"tag": "markdown", "content": "📌**xxxxxxxxxxx**"},
            {
                "alt": {"content": "", "tag": "plain_text"},
                "img_key": "${Picture_1}",
                "tag": "img",
                "mode": "fit_horizontal",
                "compact_width": False,
            },
            {"tag": "hr"},
            {"tag": "markdown", "content": "📌**xxxxxxxxxxx**"},
            {
                "tag": "img",
                "img_key": "${Picture_2}",
                "alt": {"tag": "plain_text", "content": ""},
                "mode": "fit_horizontal",
                "preview": True,
                "compact_width": False,
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "点击查看更多详情"},
                        "type": "primary",
                        "multi_url": {
                            "url": "https://lotuscars.feishu.cn/sheets/xxxxxxxxx",
                            "pc_url": "",
                            "android_url": "",
                            "ios_url": "",
                        },
                    }
                ],
            },
            {"tag": "div", "text": {"content": "<at id=all></at>", "tag": "lark_md"}},
        ],
    }

    def __init__(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/t-g1046gmM2EQ7URC6AGCFHYHA6V5HPMEBI6ZOBKV6"
        payload_data = {"app_id": self.app_id, "app_secret": self.app_secret}
        response = requests.post(
            url=url, data=json.dumps(payload_data), headers=self.headers
        ).json()
        self.token = response["tenant_access_token"]

    def uploadImage(self, picture_path):
        get_image_key_url = "https://open.feishu.cn/open-apis/im/v1/img_v3_02bt_dd221dc7-21aa-4507-877d-4ef36a7c560g"
        form = {
            "image_type": "message",
            "image": (open(picture_path, "rb")),
        }  # 需要替换具体的path
        multi_form = MultipartEncoder(form)
        image_key_headers = {
            "Authorization": "Bearer " + self.token,
        }
        image_key_headers["Content-Type"] = multi_form.content_type
        response = requests.request(
            "POST", get_image_key_url, headers=image_key_headers, data=multi_form
        )
        content = json.loads(response.content)
        img_key = str(content["data"]["image_key"])
        print(response.headers["X-Tt-Logid"])  # for debug or oncall
        print(f"The img_key is {img_key}")  # Print Response
        return img_key

    def send_msg_talk(self, picture1_img_key, picture2_img_key):
        self.json_data["elements"][1]["img_key"] = picture1_img_key
        self.json_data["elements"][4]["img_key"] = picture2_img_key
        msg_card = json.dumps(self.json_data)
        body = json.dumps({"msg_type": "interactive", "card": msg_card})
        response = requests.post(url=self.chatGPT_url, data=body, headers=self.headers)
        print(response)
