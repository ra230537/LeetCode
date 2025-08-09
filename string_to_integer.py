class Solution:
    def ignore_lead_zeros(self, s) -> str:
        for idx in range(len(s)):
            if (s[idx] != '0'):
                return s[idx:]
        return '0'
    def ignore_char(self, s) -> str:
        for idx in range(len(s)):
            if (not self.is_number(s[idx])):
                if (len(s[:idx]) > 0):
                    return s[:idx]
                else:
                    return '0'
        return s
    def is_minus(self, s: str) -> int:
        if s[0] == '-':
            if (len(s) == 1):
                return False
            elif(self.is_number(s[1])):
                return True
        return False
    def has_positive_sign(self, s: str) -> int:
        if s[0] == '+':
            if (len(s) == 1):
                return False
            elif(self.is_number(s[1])):
                return True
        return False
    def is_number(self, char):
        return ord(char) - ord('0') <= 9 and ord(char) - ord('0') >= 0 
    def convert_to_integer(self, s, is_minus) -> int:
        size_s = len(s)
        response = 0
        for idx, char in enumerate(s):
            number = ord(char) - ord('0')
            size_order = size_s - idx - 1
            if (size_order > 9 ):
                if (is_minus):
                    return -2**31
                else:
                    return 2**31 - 1
            response += number * (10 ** size_order)

        response = -response if is_minus else response
        if response > 2**31-1:
            response = 2**31-1
        if response < -2**31:
            response = -2**31
        return response
    def myAtoi(self, s: str) -> int:
        # ignore white space
        s = s.strip()
        if (s == ''):
            return 0
        is_minus = self.is_minus(s)
        has_positive = self.has_positive_sign(s)
        if (is_minus or has_positive):
            s = s[1:]
        s = self.ignore_char(s)
        s = self.ignore_lead_zeros(s)
        return self.convert_to_integer(s, is_minus)
    
'''Se atentar aos casos de borda: +1, -42a, +-1, -, "",000003, abcoi,123 abc, abc 123 '''