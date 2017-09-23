from html.parser import HTMLParser


def get_href(attrs):
    if len(attrs) == 0:
        return ""

    for k, v in attrs:
        if k == 'href':
            return v

    return ""


class IndexParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            link = get_href(attrs)
            print(link)
            if link != '' and self.links.count(link) <= 0:
                self.links.append(link)


def index_parser(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        html = ""
        for line in f.readlines():
            html += line

        parser = IndexParser()
        parser.feed(html)
        return parser.links


if __name__ == "__main__":
    text = index_parser("index.html")
    print(text)
