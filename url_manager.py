# url调度管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self,url):
        """
        添加一个新连接
        :return:
        """
        pass
    def has_new_url(self):
        """
        还有没有待爬取的url
        :return:
        """
        pass
    def get_new_url(self):
        """
        去一个新的url准备请求他

        :return:
        """

    def add_new_urls(self,urls):
        """
        一个词条上所有连接添加入self.new_urls中
        :return:
        """
        pass