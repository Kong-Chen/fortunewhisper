import requests

def get_coupon_list(channel_access_token):
    url = "https://api.line.me/v2/bot/user/coupon/list"
    headers = {
        "Authorization": "Bearer " + channel_access_token,
    }
    response = requests.post(url, headers=headers)
    return response.json()


if __name__ == "__main__":
    channel_access_token = "hVWjBb2PvHeTzCxh0wEb1cBacym2FNHcrUuvOvNwg3kQ2O0KXxm8PrGwz/9NcqKN/rimWB/xiQb56rD5ZJmxTpD0f64rvG+fWFdxG6a/iDE5/g34VziE/9l29jLKCmGgY4VBii154CXVRcMdXDXkZAdB04t89/1O/w1cDnyilFU="
    coupon_list = get_coupon_list(channel_access_token)
    print(coupon_list)