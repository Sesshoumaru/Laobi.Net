from html.parser import  HTMLParser

class IndexParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.body_text = ""
        self.body_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.body_tag = True

    def handle_endtag(self, tag):
        if tag == "body":
            self.body_tag = False

    def handle_data(self, data):
        if self.body_tag:
            self.body_text += data

def index_parser(file_name):
    with open(file_name,'r',encoding='UTF-8') as f:
        html = ""
        for line in f.readlines():
            html+= line

        parser = IndexParser()
        parser.feed(html)
        return parser.body_text


if __name__ == "__main__":
    text = index_parser("index.html")
    print(text)