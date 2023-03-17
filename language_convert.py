
def convert_to_chinese(value):
    print(value.encode('ascii').decode('unicode_escape'))
    pass

if __name__ == '__main__':
    value = r'\u5cf0\u5934\u3002\n\u6c14\u606f\u60a0\u957f\u6101\u610f\u5c11\uff0c\u601d\u7ef4\u7eb7\u7e41\u68a6\u4e2d\u6e38\u3002'
    convert_to_chinese(value)
