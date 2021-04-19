import bisect


class AssignCookie:
    def getContentChildren(self, children: list, cookies: list) -> int:
        children.sort(reverse=True)
        cookies.sort(reverse=True)
        result = 0
        for child in children:
            for size in cookies:
                if size >= child:
                    result += 1
                    cookies.remove(size)
                    break

        return result

    def getContentChildren_binary(self, children: list, cookies: list) -> int:
        children.sort()
        cookies.sort()

        result = 0
        for i in cookies:
            #'Find rightmost value less than or equal to x'
            index = bisect.bisect_right(children, i)
            if index > result:
                result += 1

        return result


instance = AssignCookie()
print(instance.getContentChildren([1, 2], [1, 2, 3]))
print(instance.getContentChildren_binary([1, 4, 4, 2], [1, 2, 3]))
