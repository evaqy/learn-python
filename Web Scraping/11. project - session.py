#利⽤session实现发布⾖瓣读书个⼈中⼼⽣活点滴
url = 'https://www.douban.com/'

import requests

url_login = "https://lp.open.weixin.qq.com/connect/l/qrconnect?uuid=061VYk2iLydzXL8H&last=404&_=1589934873249"

headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

login_data = {
    "uuid": "061VYk2iLydzXL8H",
    "last": "404",
    "_": "1589934873249"
}

login_response = requests.post(url=url_login,headers=headers,data=login_data)
#print(login_response)
cookie = login_response.cookies

comment_url = "https://www.douban.com/"
comment_data = {
    "ck": "z4Uc",
    "comment": input("分享一句生活点滴"),
    "privacy_and_reply_limit": "P",
}
comment_response = requests.post(comment_url, headers=headers, data=comment_data, cookies=cookie)
print(comment_response.status_code)

# import requests

# session = requests.session()

# comment_url = "https://www.douban.com/"

# headers = {
#     'Cookie': 'bid=Z2WVCBkibH4; __gads=ID=50beac6f881f5ffe:T=1587229508:S=ALNI_MagEbQ3BvwQhKSRYLy7Ptud1z4Wug; _vwo_uuid_v2=DCF7A94E8A458E9CA88EC25D1B53DE1A8|03fadfca1d9d33bde3a2be073c750cbf; gr_user_id=9749a845-bd4e-4017-a802-c154d7821952; __qca=P0-1366576094-1588287202671; __utmc=30149280; ll="108258"; _pk_ses.100001.8cb4=*; __utma=30149280.489049458.1587229506.1589913836.1589934767.7; __utmz=30149280.1589934767.7.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; viewed="34884579_1269900_25799956_21057430_2891205_27153403"; dbcl2="173147345:rVoXxn7bmoI"; ck=z4Uc; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17314; DigiTrust.v1.identity=eyJpZCI6Ikk2Rk9hVG9jd3UyWHdIZ0dHamRYdlI3S1pMMExXVEdwWmJFUjB4MC8xYW9VZkorbGZXRWpmRDhrM0s2cVlCSUExQktNcVpCV0FKQmRZQVkvZEtITk1uR1ZWMVdqQ3Q1TGF0R1lJSFRleElLNDZENzB3U28xbUJSTS90VGIyTnlWdWtZcTZNUUE0Z1lZYVZrRitXbWVxVnM0QkVJSm92NURkVjdEbThBSEw0Vk5XUnRoL25GRitXK2Jlck43cnptWVhPK0Ftdk16bkw2a0RDNlpBMDNUMXZvYnVDOENPSVJBamozYWRveThzcWlIZld3ZGJzSGR5WTRTYlZqbkhWU0dTUmxjVkxuRGRSMVRLcEhpOEE5ZkY3WnVpV0dMbmJJaDFaVm1ON1o1YmU0d2p0djk4em02ZGhpOHkrZmtCOU5rQmNoWGI1cEVsTE01V2lLM2w3OUVEUT09IiwidmVyc2lvbiI6MiwicHJvZHVjZXIiOiIxQ3JzZFVOQW82IiwicHJpdmFjeSI6eyJvcHRvdXQiOmZhbHNlfSwia2V5diI6NH0%3D; ucfunnel_uid=d394af49-0e3f-30ed-938d-cc0be419a920; _pk_id.100001.8cb4=8a8eb608bc1b8a80.1589913833.2.1589936604.1589913833.; __utmb=30149280.23.10.1589934767; GED_PLAYLIST_ACTIVITY=W3sidSI6IlIxL2YiLCJ0c2wiOjE1ODk5Mzc5OTcsIm52IjoxLCJ1cHQiOjE1ODk5MzY2MDYsImx0IjoxNTg5OTM3OTkzfV0.'
# }

# comment_data = {
#     "ck": "z4Uc",
#     "comment": input("分享一句生活点滴:"),
#     "privacy_and_reply_limit": "P",
# }

# comment_response = requests.post(comment_url, headers=headers, data=comment_data)
# print(comment_response.status_code)