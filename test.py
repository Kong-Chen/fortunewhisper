from linebot import LineBotApi
from linebot.models import TextMessage

# 替換成您自己的Channel Access Token
channel_access_token = 'czH9a2VRdE4WY0n031h2sMjVEs979haELbdnS1QTvd8WooM7wMtulpBp1sTMqDua60W0Gq6M0oo+gH6hkcfAuyTiUFjq1Xrlhi+Pkts+9p9AsbdGNqAO2oGhK3AlGhZuf9NKV+QVtUTENFTWJG0wNAdB04t89/1O/w1cDnyilFU='

# 初始化LineBotApi
line_bot_api = LineBotApi(channel_access_token)

# 要推送的消息內容
message = '這是一則Line推送消息'

# 目標用戶的Line User ID（可以是單個用戶或多個用戶的列表）
user_id = 'Ud91537b73f965b281b99f822c9e3387e'

try:
    # 使用LineBotApi向用戶推送消息
    line_bot_api.push_message(user_id, TextMessage(text=message))
    print('消息已成功推送！')
except Exception as e:
    # 處理錯誤
    print('消息推送失敗：', e)
