class Htmloutputer(object):
    def __init__(self):
        self.datas=[]    #类里面的全局变量,现存一个数据备份,共output等函数使用.

    def collect_data(self,new_url,new_data):
        assert new_url is not None
        assert new_data is not None

        self.datas.append((new_url,new_data))



    def output_html(self):
        """
        输出到output.html
        :return:
        """

        file = open('output.html',mode='w')
        # 从这个例子可以看出django的模板渲染语言原理
        file.write("<html>")
        file.write("<body>")
        for row in self.datas:
            file.write("<tr>")
            file.write(f"<td>{row[0]}</td><br>")
            file.write(f"<td>{row[1]['title']}</td><br>")
            file.write(f"<td>{row[1]['summary']}</td><br>")

            file.write("</tr>")
        file.write("</body>")
        file.write("</html>")


    def save_db(self):
        """保存到数据库"""
        pass