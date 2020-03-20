#utf-8
import requests
url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?' \
      'leftTicketDTO.train_date=2020-02-01&' \
      'leftTicketDTO.from_station=SHH&' \
      'leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
response=requests.get(url)
response.encoding=response.apparent_encoding
print(response.text)
# url='https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
