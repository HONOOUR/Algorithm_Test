from collections import deque


class ValidPalindrome:

    def init(self, s: str) -> list:
        array = []
        for char in s:
            if char.isalnum():
                array.append(char.lower())

        return array

    def isPalindrome(self, s: str) -> bool:
        array = self.init(s)
        return array == array[::-1]

    def isPalindrome_deque(self, s: list) -> bool:
        dqueue = deque()
        for char in s:
            dqueue.append(char.lower())

        while len(dqueue) > 1:
            if dqueue.popleft() != dqueue.pop():
                return False

        return True


item = "applelppa"
palindrome = ValidPalindrome()
is_palindrome = palindrome.isPalindrome(item)
print(is_palindrome)
is_palindrome = palindrome.isPalindrome_deque(item)
print(is_palindrome)
