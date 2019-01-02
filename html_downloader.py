# 下载器
import requests

class HtmlDowndloader(object):
    def download(self,url):
        assert url is not None,"download()方法参数url不能为None"

        # if url is None:
        #     raise Exception


        headers = {
            'Host':'gsp0.baidu.com',
            'Refer':'https://baike.baidu.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

        response = requests.get(url,headers=headers)
        if response.status_code != 200:
            raise Exception(f'请求失败,code{response.status_code}')

        return response.text
