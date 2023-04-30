roman = input("""
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    Please enter roman numeral symbols: """)

class Solution:
    def romanToInt(self, s: str) -> int:

        """Dictionary"""
        roman_symbol = {
            'I': '1', 'V': '5', 'X': '10', 'L': '50',
            'C': '100', 'D': '500', 'M': '1000'
        }

        """Recognizing Values"""
        list_value = []
        list_roman = list(s)
        for ele in list_roman:
            list_value.append(roman_symbol[ele])
        # print(list_value)
        # print(list_roman)

        """Culculating Vlaues"""
        add = []
        minus = []
        for i in range(len(list_value)-1):
            if int(list_value[i]) < int(list_value[i+1]):
                minus.append(int(list_value[i]))
                # print(list_value[i],'-')

            elif int(list_value[i]) >= int(list_value[i+1]):
                add.append(int(list_value[i]))
                # print(list_value[i],'+')
        add.append(int(list_value[-1])) # the last one must be add
        # print(add, minus)
        consequece = sum(add) - sum(minus)
        print('The value of',roman, 'is', consequece)

result = Solution()
result.romanToInt(roman)

