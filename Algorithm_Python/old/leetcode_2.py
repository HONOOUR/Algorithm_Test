# 211 design add and search words data structure
# addWord(word)
# search(word)

class WordDictionary:
    def __init__(self):
        # dic = { bad, b.., .a., ...}
        self.dic = set()

    def addWord(self, word: str) -> None:
        def dfs_addWord(selected, dot_count, visited, word):
            if len(selected) > dot_count:
                return
            # key
            # <bad>
            # .ad
            # b.d
            # ba.
            # ..d
            # .a.
            # b..

            if len(selected) == dot_count:
                temp = list(word)
                for i in selected:
                    temp[i] = '.'
                answer = ''
                for t in temp:
                    answer += t

                self.dic.add(answer)

            first_index = 0
            if len(selected) > 0:
                first_index = selected[-1]

            for i in range(first_index, len(word)):
                if i in visited:
                    continue

                visited.add(i)
                selected.append(i)
                dfs_addWord(selected, dot_count, visited, word)
                selected.pop(-1)
                visited.remove(i)

            # 한 단어 dfs -> . 추가해서 넣기
            # 한 개 뽑기, 두 개 뽑기 .. 전체 길이-1 개 뽑기 -> 뽑아서 str[i] = '.'
        visited = set()
        for dot_count in range(0, len(word)+1):
            dfs_addWord([], dot_count, visited, word)

    def search(self, word: str) -> bool:
        # search with dot
        if word in self.dic:
            return True
        else:
            return False


wordDictionary = WordDictionary()
wordDictionary.addWord('a')
print(wordDictionary.search('.'))


# 212 word search
def dfs_word(y, x, index, temp, word, visited, board):
    answer = ''
    if temp == word:
        return word
    # if the next index is bigger than the length of the word
    if index+1 >= len(word):
        return answer

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
            if visited[ny][nx] == 1:
                continue

            if temp + board[ny][nx] == word:
                return word
            elif board[ny][nx] == word[index+1]:
                visited[ny][nx] = 1
                if len(dfs_word(ny, nx, index+1, temp + board[ny][nx], word, visited, board)) > 0:
                    answer = word
                visited[ny][nx] = 0
    return answer


def findWords(board, words):
    answers = []
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    words.sort()
    for word in words:
        for y in range(len(board)):
            for x in range(len(board[0])):
                # find first letter
                if word[0] == board[y][x]:
                    visited[y][x] = 1
                    # depth search (find the next letter with the index+1)
                    if len(dfs_word(y, x, 0, board[y][x], word, visited, board)) > 0 and word not in answers:
                        answers.append(word)
                    visited[y][x] = 0
    return answers


findWords([["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]], ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
          )
# findWords([["a", "b"], ["c", "d"]], ["abcb"])

# findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"])
