import re
import requests

class Notice:
    @staticmethod
    def serverJ(push_key, title, content):
        if not push_key:
            return
        desp = content.replace("\n", "\n\n")
        data = {"text": title, "desp": desp}
        match = re.match(r"sctp(\d+)t", push_key)
        if match:
            url = f"https://{match.group(1)}.push.ft07.com/send/{push_key}.send"
        else:
            url = f"https://sctapi.ftqq.com/{push_key}.send"
        try:
            requests.post(url, data=data, timeout=15)
        except Exception as e:
            print(f"Server酱通知失败: {e}")