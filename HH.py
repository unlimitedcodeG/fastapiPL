import requests
from requests_toolbelt import MultipartEncoder

# 输入pip install requests_toolbelt 安装依赖库


def uploadImage():
    url = "https://open.feishu.cn/open-apis/im/v1/images"
    form = {
        "image_type": "message",
        "image": (open("profile.jpg", "rb")),
    }  # 需要替换具体的path
    multi_form = MultipartEncoder(form)
    headers = {
        "Authorization": "Bearer t-g1046gmM2EQ7URC6AGCFHYHA6V5HPMEBI6ZOBKV6",  ## 获取tenant_access_token, 需要替换为实际的token
    }
    headers["Content-Type"] = multi_form.content_type
    response = requests.request("POST", url, headers=headers, data=multi_form)
    print(response.headers["X-Tt-Logid"])  # for debug or oncall
    print(response.content)  # Print Response


if __name__ == "__main__":
    uploadImage()
