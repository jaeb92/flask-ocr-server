import re


class RegExpression():
    name_pattern = r"[가-힣]{2,5}"
    school_pattern = r"[가-힣]{2,}[대학교|대학]$"
    date_pattern = r"\d+년[\s|.|-]?\d+월[\s|.|-]?\d+일"

    def __init__(self):
        pass

    @staticmethod
    def set_compile(pattern):
        return re.compile(pattern)

    def find_name(self, t):
        print(f'input text={t}')
        c = self.set_compile(self.name_pattern)
        result = c.findall(t)
        print(f'find result={result}')
        return result

    def find_school(self, t):
        print(f'input text={t}')
        c = self.set_compile(self.school_pattern)
        result = c.findall(t)
        print(f'find result={result}')
        return result

    def find_date(self, t):
        print(f'input text={t}')
        c = self.set_compile(self.date_pattern)
        result = c.findall(t)
        print(f'find result={result}')
        return result


if __name__ == "__main__":
    regex = RegExpression()
    text = "홍길동 서울대학교 2021년12월 31일"

    n = regex.find_name(text)
    s = regex.find_school(text)
    d = regex.find_date(text)
