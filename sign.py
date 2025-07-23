import os
import requests

def main():
    # 从 Secrets 读取 Cookie 或 URL
    auth_data = os.getenv("QUARK_COOKIE")  
    accounts = auth_data.split("#")  # 多账号分隔符
    
    for i, cookie in enumerate(accounts):
        # 调用签到接口
        headers = {"Cookie": cookie.strip()}
        url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/sign"
        resp = requests.post(url, headers=headers).json()
        
        # 解析结果
        if resp.get("code") == 0:
            reward = resp["data"]["sign_daily_reward"] / 1048576  # 转换为 MB
            print(f"账号{i+1}：签到成功，获得 {reward}MB 空间")
        else:
            print(f"账号{i+1}：失败，原因：{resp.get('message')}")

if __name__ == "__main__":
    main()