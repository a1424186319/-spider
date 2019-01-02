from lxml import etree

class HtmlParser(object):
    def parse(self,html_content):
        """
        # 接受网页的html响应,解析,获取想要的数据
        :param html_content: {str}'<html></html>'
        :return: {list}['https://baike.com/item/某一词条/31321']
        :return: {dict}{'title':title,'summary':summary}
        """

        assert html_content is not None,"html_content为空 请检查"

        dom = etree.HTML(html_content)

        pattern_title = '//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()'
        pattern_summer = '//div[@class="lemma-summary"]/div/text()'
        pattern_href = '//div[@class="main-content"]//a[@target="_blank"]/@href'

        title = dom.xpath(pattern_title)[0]
        summary  =dom.xpath(pattern_summer)[0]
        new_urls = dom.xpath(pattern_href)

        for index,href in enumerate(new_urls):
            # todo 判断连接是否合法,可以用正则或者str.find('item)
            new_urls[index]='https://baike.baidu.com'+str(href)



        # return title,summary,new_urls
        # context = {}
        # context['title']=title
        # context['summary']=summary
        # context['new_urls']=new_urls
        # return context

        new_data = {'title':title,'summary':summary}
        return new_urls,new_data

