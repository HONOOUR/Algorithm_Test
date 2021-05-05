class HashPractice:
    def getParticipantNotComplete(self, participate, completion):
        # 같은 이름으로 분리
        participate_hash = {}
        for par in participate:
            if par not in participate_hash:
                participate_hash[par] = 1
            else:
                participate_hash[par] += 1

        # search completion in participate then one left
        for com in completion:
            if com in participate_hash:
                participate_hash[com] -= 1

        for (par, num) in participate_hash.items():
            if num > 0:
                return par

    def isNotPhonebookHead(self, phone_book):
        for i in range(len(phone_book)):
            for j in range(len(phone_book)):
                index = (i + j) % len(phone_book)
                if i == index:
                    continue
                length = len(phone_book[i])
                if phone_book[i] == phone_book[index][:length]:
                    return False

        return True


instance = HashPractice()
participate = ["leo", "kiki", "eden", "kiki"]
completion = ["eden", "kiki", "leo"]
print(instance.getParticipantNotComplete(participate, completion))
# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["1234", "123", "12", "567", "88"]
print(instance.isNotPhonebookHead(phone_book))
