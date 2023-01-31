# coding:utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkalimt.request.v20181012 import TranslateRequest
import json
import queue


print("欢迎使用翻译软件！".center(60, '-'))
print("作者：XXX".center(60))
print("需要进行翻译的文本输入完毕后，请输入“Exit”退出程序。".center(60))
print("默认为中英互译，如需其他语言互译，请输入对应语言代码。".center(60))
print("更换语言请输入“Change”".center(60))
print("-" * 60)
print("语言代码如下：")
print("中文：zh")
print("英文：en")
print("日文：ja")
print("韩文：ko")
print("法文：fr")
print("繁体中文：zh-tw")
print("俄语：ru")
print("-" * 60)
source = input("请输入源语言代码：默认为中文：\n")
if source == "":
    source = "zh"
source = source.lower()
target = input("请输入目标语言代码：默认为英文：\n")
if target == "":
    target = "en"
target = target.lower()

print("您选择的源语言是：", source)
print("您选择的目标语言是：", target)


def translate(text, source, target):
    # 创建AcsClient实例
    client = AcsClient(
        "XXXXXXX",  # 阿里云账号的AccessKey ID
        "XXXXXXXX",  # 阿里云账号Access Key Secret
        "cn-beijing"  # 地域ID
    );
    # 创建request，并设置参数
    request = TranslateRequest.TranslateRequest()
    request.set_SourceLanguage(source)  # 源语言
    request.set_Scene("title")  # 设置场景，商品标题：title，商品描述：description，商品沟通：communication
    request.set_SourceText(text)  # 原文
    request.set_FormatType("text")  # 翻译文本的格式
    request.set_TargetLanguage(target)  # 目标语言
    request.set_method("POST")
    # 发起API请求并显示返回值
    response = client.do_action_with_exception(request)
    # print(json.loads(response))  # 测试打印返回值
    print("*" * 60)
    print(json.loads(response)["Data"]["Translated"])  # 打印翻译后的文本
    print("*" * 60)

def changeLanguage():
    source = input("请输入源语言代码：默认为中文：\n")
    if source == "":
        source = "zh"
    source = source.lower()
    target = input("请输入目标语言代码：默认为英文：\n")
    if target == "":
        target = "en"
    target = target.lower()
    print("您选择的源语言是：", source)
    print("您选择的目标语言是：", target)
    return source, target

while True:
    text = input("请输入要翻译的文本：")
    if text == "Exit":
        break
    elif text == "Change":
        source, target = changeLanguage()
        text = input("请输入要翻译的文本：")
    translate(text, source, target)
input('Press Enter to exit...')
