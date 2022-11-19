class Solution:
    R = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        return self.tail(s, 0)

    def tail(self, s: str, sum: int) -> int:
        if len(s) == 0:
            return sum
        if len(s) > 1:
            last_two = s[-2:]
            if last_two in self.R:
                return self.tail(s[:-2], sum + self.R[last_two])
            else:
                return self.tail(s[:-1], sum + self.R[s[-1]])
        else:
            return sum + self.R[s[-1]]


class Solution2:
    R = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        return self.tail(s, 0)

    def tail(self, s: str, sum: int) -> int:
        if len(s) == 0:
            return sum

        if len(s) > 1:
            value = self.R[s[-1]]
            prev_value = self.R[s[-2]]
            if prev_value == value / 5 or prev_value == value / 10:
                return self.tail(s[:-2], sum + value - prev_value)
            else:
                return self.tail(s[:-1], sum + value)
        else:
            return sum + self.R[s[-1]]


if __name__ == "__main__":
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))
    print(Solution2().romanToInt("III"))
    print(Solution2().romanToInt("IV"))
    print(Solution2().romanToInt("LVIII"))
    print(Solution2().romanToInt("MCMXCIV"))
