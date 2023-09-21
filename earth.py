import requests

# API 密鑰
api_key = "74K2SccksUYY9UL8P6FPb7oz3Vn0JFacjP5ZPdPh"

# API 網址
url = "https://api.nasa.gov/planetary/apod"

# API 參數
params = {
    "api_key": api_key
}

# 發送 API 請求
response = requests.get(url, params=params)

# 取得 API 的返回值
data = response.json()

# 顯示照片的網址
print("Picture URL:", data["url"])