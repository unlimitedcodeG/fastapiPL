import requests
import json
from datetime import datetime

# 获取当前时间并格式化
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
## 替换为你的自定义机器人的 webhook 地址。
WEBHOOK_URL = (
    "https://open.feishu.cn/open-apis/bot/v2/hook/beb036b7-9947-4dd6-a05e-04222322fdc4"
)
## 将消息卡片内容粘贴至此处。
card_json = {
    "config": {},
    "i18n_elements": {
        "en_us": [
            {
                "tag": "column_set",
                "flex_mode": "none",
                "background_style": "default",
                "horizontal_spacing": "8px",
                "horizontal_align": "left",
                "columns": [
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "column_set",
                                "flex_mode": "none",
                                "background_style": "default",
                                "horizontal_spacing": "8px",
                                "horizontal_align": "left",
                                "columns": [
                                    {
                                        "tag": "column",
                                        "width": "auto",
                                        "vertical_align": "center",
                                        "vertical_spacing": "8px",
                                        "background_style": "default",
                                        "elements": [
                                            {
                                                "tag": "img",
                                                "img_key": "img_v2_136e4af5-9893-4f96-a52a-60bb9b6347cg",
                                                "preview": True,
                                                "scale_type": "crop_center",
                                                "size": "tiny",
                                                "alt": {
                                                    "tag": "plain_text",
                                                    "content": "",
                                                },
                                            }
                                        ],
                                    },
                                    {
                                        "tag": "column",
                                        "width": "weighted",
                                        "vertical_align": "top",
                                        "vertical_spacing": "8px",
                                        "background_style": "default",
                                        "elements": [
                                            {
                                                "tag": "column_set",
                                                "flex_mode": "none",
                                                "horizontal_spacing": "default",
                                                "background_style": "default",
                                                "columns": [
                                                    {
                                                        "tag": "column",
                                                        "elements": [
                                                            {
                                                                "tag": "div",
                                                                "text": {
                                                                    "tag": "plain_text",
                                                                    "content": "2023 年 11 月 11 日 10:00",
                                                                },
                                                            }
                                                        ],
                                                        "width": "weighted",
                                                        "weight": 1,
                                                    }
                                                ],
                                            }
                                        ],
                                        "weight": 1,
                                    },
                                ],
                            },
                            {
                                "tag": "column_set",
                                "flex_mode": "none",
                                "background_style": "default",
                                "horizontal_spacing": "8px",
                                "horizontal_align": "left",
                                "columns": [
                                    {
                                        "tag": "column",
                                        "width": "auto",
                                        "vertical_align": "center",
                                        "vertical_spacing": "8px",
                                        "background_style": "default",
                                        "elements": [
                                            {
                                                "tag": "img",
                                                "img_key": "img_v2_f9d63232-61ec-44f0-9fb7-bf8ba82ea92g",
                                                "preview": True,
                                                "scale_type": "crop_center",
                                                "size": "tiny",
                                                "alt": {
                                                    "tag": "plain_text",
                                                    "content": "",
                                                },
                                            }
                                        ],
                                    },
                                    {
                                        "tag": "column",
                                        "width": "weighted",
                                        "vertical_align": "top",
                                        "vertical_spacing": "8px",
                                        "background_style": "default",
                                        "elements": [
                                            {
                                                "tag": "column_set",
                                                "flex_mode": "none",
                                                "horizontal_spacing": "default",
                                                "background_style": "default",
                                                "columns": [
                                                    {
                                                        "tag": "column",
                                                        "elements": [
                                                            {
                                                                "tag": "div",
                                                                "text": {
                                                                    "tag": "plain_text",
                                                                    "content": "北京学清嘉创大厦 B 座 F2-26",
                                                                },
                                                            }
                                                        ],
                                                        "width": "weighted",
                                                        "weight": 1,
                                                    }
                                                ],
                                            }
                                        ],
                                        "weight": 1,
                                    },
                                ],
                            },
                        ],
                        "weight": 1,
                    },
                    {
                        "tag": "column",
                        "width": "auto",
                        "vertical_align": "center",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "🔥立即查看"},
                                "type": "laser",
                                "complex_interaction": True,
                            }
                        ],
                    },
                ],
            },
            {
                "tag": "img",
                "img_key": "img_v2_609930d7-21cc-475a-baba-3de5dafe079g",
                "preview": True,
                "scale_type": "fit_horizontal",
                "alt": {"tag": "plain_text", "content": ""},
            },
        ],
        "zh_cn": [
            {
                "tag": "img",
                "img_key": "img_v3_02bu_55631821-5541-4ebc-b4fe-ae5ee14ff09g",
                "preview": True,
                "scale_type": "crop_center",
                "size": "stretch_without_padding",
                "alt": {"tag": "plain_text", "content": ""},
            },
            {
                "tag": "markdown",
                "content": "性能测试已经结束了，各位可以看到这次快速比对的内容",
                "text_align": "left",
                "text_size": "normal",
            },
            {
                "tag": "column_set",
                "flex_mode": "none",
                "background_style": "default",
                "horizontal_spacing": "8px",
                "horizontal_align": "left",
                "columns": [
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "markdown",
                                "content": f"**比对完成时间{current_time}**",
                                "text_align": "left",
                                "text_size": "normal",
                                "icon": {
                                    "tag": "standard_icon",
                                    "token": "time_outlined",
                                    "color": "grey",
                                },
                            }
                        ],
                        "weight": 1,
                    },
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "column_set",
                                "flex_mode": "none",
                                "horizontal_spacing": "default",
                                "background_style": "default",
                                "columns": [
                                    {
                                        "tag": "column",
                                        "elements": [
                                            {
                                                "tag": "div",
                                                "text": {
                                                    "tag": "plain_text",
                                                    "content": "jenkins-workFlow",
                                                    "text_size": "normal",
                                                    "text_align": "left",
                                                    "text_color": "default",
                                                },
                                                "icon": {
                                                    "tag": "standard_icon",
                                                    "token": "collection_outlined",
                                                    "color": "grey",
                                                },
                                            }
                                        ],
                                        "width": "weighted",
                                        "weight": 1,
                                    }
                                ],
                            }
                        ],
                        "weight": 1,
                    },
                ],
                "margin": "16px 0px 0px 0px",
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "🌠去jenkins查看"},
                        "type": "laser",
                        "complex_interaction": True,
                        "size": "medium",
                        "multi_url": {
                            "url": "https://bytedance.larkoffice.com/wiki/BG4XwdGyFiC9EikdJmQc5ozinOd",
                            "pc_url": "",
                            "ios_url": "",
                            "android_url": "",
                        },
                    }
                ],
            },
            {
                "tag": "note",
                "elements": [
                    {"tag": "standard_icon", "token": "robot-add_outlined"},
                    {"tag": "plain_text", "content": "如有疑问，请咨询刘泓与彭美霖"},
                ],
            },
        ],
    },
    "i18n_header": {
        # "en_us": {
        #     "title": {"tag": "plain_text", "content": "十周年庆典"},
        #     "subtitle": {"tag": "plain_text", "content": ""},
        #     "template": "default",
        #     "icon": {
        #         "tag": "custom_icon",
        #         "img_key": "img_v2_1bfeb6af-dd10-4e49-8fd2-5a392bc86ccg",
        #     },
        # },
        "zh_cn": {
            "title": {
                "tag": "plain_text",
                "content": "创游世界性能测试快速对比结束，快来查看测试结果吧！",
            },
            "subtitle": {"tag": "plain_text", "content": ""},
            "template": "blue",
            "icon": {
                "tag": "custom_icon",
                "img_key": "img_v3_02bu_52d0119c-f2f1-4e5b-bacd-2ea2651cca7g",
            },
        },
    },
}
body = json.dumps({"msg_type": "interactive", "card": card_json})
print(body)
print("sad ")
headers = {"Content-Type": "application/json"}
res = requests.post(url=WEBHOOK_URL, data=body, headers=headers)
print(res.request.body)
print(res.text)
