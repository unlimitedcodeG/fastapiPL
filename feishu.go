package main

import (
	"fmt"

	"github.com/junhaideng/feishu-group-robot/msg"
	"github.com/junhaideng/feishu-group-robot/utils"
)

// webhook url
var webhook string

// 数字签名
var secret string

func init() {
	webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/beb036b7-9947-4dd6-a05e-04222322fdc4"
	secret = "pxoSWVzWzlWKg5UpW5qwc"
}

func main() {
	sendCardMsg()
}

// 发送图片消息
func sendImageMsg() {
	m := msg.NewImageMsg("img_ecffc3b9-8f14-400f-a014-05eca1a4310g")
	fmt.Println(utils.SendMsg(webhook, m))
}

// 使用签名验证的图片消息
func sendImageMsgWithSign() {
	m := msg.NewImageMsgWithSign(secret, "img_ecffc3b9-8f14-400f-a014-05eca1a4310g")
	fmt.Println(utils.SendMsg(webhook, m))
}

func sendShareChatMsg() {
	m := msg.NewShareChatMsg("oc_f5b1a7eb27ae2c7b6adc2a74faf339ff")
	fmt.Println(utils.SendMsg(webhook, m))
}

func sendPostMsg() {
	m := msg.NewPostMsg("post msg")
	m.AddText("hi, welcome ")
	m.AddLink("here", "https://github.com/junhaideng")
	fmt.Println(utils.SendMsg(webhook, m))
}

func sendTextMsg() {
	m := msg.NewTextMsg("hello world")
	fmt.Println(utils.SendMsg(webhook, m))
}

func sendCardMsg() {
	m := msg.NewCardMsg("just a test")
	m.AddElement("a pure **test**, use any markdown syntax you like")
	fmt.Println(utils.SendMsg(webhook, m))
}

func sendTextMsgWithSign() {
	m := msg.NewTextMsgWithSign(secret, "hello world")
	fmt.Println(utils.SendMsg(webhook, m))
}
