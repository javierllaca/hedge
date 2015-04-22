from re     import match as is_match, sub as replace
from sys    import stdin

def parse_xml():
    """Parse xml and print only content enclosed in <post> tags"""
    post = False
    for line in stdin:
        line = line.strip()
        if is_match(r'</post|<quote', line):
            post = False
        elif post and line:
            print replace(r'<img(.*?)/>|<a(.*?)</a>', '', line)
        elif is_match(r'<post|</quote', line):
            post = True

if __name__ == '__main__':
    parse_xml()

