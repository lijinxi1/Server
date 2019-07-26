import requests
# 携带cookie的请求地址
requests.adapters.DEFAULT_RETRIES = 5
url = "http:127.0.0.1:8000/"
# post请求的地址
post_url = "http://172.0.0.0:8000/register_result/"
# post时需要提交的数据
post_data = {"identity": "teacher", "_id": "20164859","name":"李金熹",
             "class_office":'通信1603',"email":'1819826126@qq.com',
             "phone":'13940207467','address':'五舍A'}
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36"}

# 实例化session
session = requests.session()
# 使用session获取本地的cookie
session.post(post_url, data=post_data, headers=headers)
# 再使用session请求登录后的页面
response = session.get(url, headers=headers)

with open('register_result.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())
