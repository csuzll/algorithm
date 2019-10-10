import sys

def strToInt(s):
    length = len(s)
    # 空字符串
    if length == 0:
        return 0
    # 非空字符串
    else:
        # 正负号标志位，1代表正数，-1代表负数
        flag = 1
        # 数字开始的索引值，用于区分第一位是否是符号位
        startindex = 0
        if s[0] == "+":
            flag = 1
            startindex = 1
        if s[0] == "-":
            flag = -1
            startindex = 1

        res = 0
        # 从startindex位置从前往后索引计算
        for each in s[startindex:]:
            if each >= '0' and each <= "9":
                res = res * 10 + flag * (ord(each)-ord("0"))
                # if res > sys.maxsize or res < -sys.maxsize-1:
                #     res = 0
                #     break
            else:
                res = 0
                break
    return res

if __name__ == '__main__':
    s1 = ""
    print(strToInt(s1))
    s2 = " "
    print(strToInt(s2))
    s3 = "+"
    print(strToInt(s3))
    s4 = "-"
    print(strToInt(s4))
    s5 = "123"
    print(strToInt(s5))
    s6 = "+123"
    print(strToInt(s6))
    s7 = "-123"
    print(strToInt(s7))
    s8 = "12+3"
    print(strToInt(s8))
    s9 = "12.34"
    print(strToInt(s9))
    s10 = "abcxxx"
    print(strToInt(s10))
    s11 = "0"
    print(strToInt(s11))
    s12 = "9223372036854775808" # 最大
    print(strToInt(s12))
    s13 = "-9223372036854775809" # 最小
    print(strToInt(s13))