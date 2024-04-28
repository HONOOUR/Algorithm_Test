class JewelsAndStone:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in J:
            if char in freqs:
                count += freqs[char]

        return count

    def numJewelsInStones_2(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in J:
                count += 1

        return count


instance = JewelsAndStone()
instance.numJewelsInStones("aA", "aAAbbbb")
instance.numJewelsInStones_2("aA", "aAAbbbb")
