## https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumeralsHelper:
    def __init__(self):
        self.input = None
        self.roms = {
            "CM" : 900,
            "CD" : 400,
            "XC" : 90,
            "XL" : 40, 
            "IX" : 9,
            "IV" : 4,
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1,
        }

    def to_roman(self, data):
        self.input, large, new_char = data, 0, ''
        digit = self.input
        result = ''
        more = True
        while digit > 0:
            more = False
            for num in self.roms.items():
                if digit>=num[1]>large:
                    large = num[1]
                    new_char = num[0]
            result += new_char
            digit -= large
            large = 0
        return result
    
    def from_roman(self, data):
        self.input = data
        s = self.input
        result = 0
        for key in self.roms.keys():
            while s.find(key) > -1:
                s = s.replace(key,"",1)
                result += roms[key]
        return result
        

# year = RomanNumerals()
RomanNumerals = RomanNumeralsHelper()
# rn = RomanNumerals.to_roman(99)
# print("input \'{}\' to roman \'{}\'".format(RomanNumerals.input,rn))
# num = RomanNumerals.from_roman('XCIX')
# print("input \'{}\' to num \'{}\'".format(RomanNumerals.input,num))

print(RomanNumerals.to_roman(39)) #DCCCXCIX
print(RomanNumerals.from_roman('XXX'))