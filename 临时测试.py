from html_downloader import HtmlDowndloader

downloader = HtmlDowndloader()
html_content = downloader.download(url='https://baike.baidu.com/item/Python/407313')
print(html_content)

# 测试得响应的htmlcontent,经过比对是纯静态页面,想要的数据都已包含.