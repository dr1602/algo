str1 = 'ABCABC'
str2 = 'ABC'

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''

    def gdc(a, b):
        while b:
            print(f'this is a:', a)
            print(f'this is b: {b}')
            a, b = b, a % b
        return a

    gdc_length = gdc(len(str1), len(str2))

    return str1[:gdc_length]

result = gcdOfStrings(str1, str2)
print(result)