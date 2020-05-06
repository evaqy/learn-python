#根据已给的⽹址分析⽹站特征，将最新发布的岗位第⼀⻚的标题例如（28297-（⾼级） 海外战略分析经理）爬取到本地。
import requests

start_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1585450579819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"

response = requests.get(url=start_url)
try:
    if response.status_code == 200:
        json_response = response.json()
        list_title = json_response['Data']['Posts']
        for title in list_title:
            position_title = title['RecruitPostName']
            print(position_title)
except Exception as error:
    print(error)


