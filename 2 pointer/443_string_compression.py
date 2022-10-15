class Solution:
    def compress(self, chars: list[str]) -> int:
        l, r = 0, 0
        counter = 0
        dummy = []

        while r < len(chars):
            if chars[l] != chars[r]:
                if counter == 1:
                    dummy.append(chars[l])
                else:
                    dummy.extend([chars[l]] + list(str(counter)))
                l = r
                counter = 0
            elif chars[l] == chars[r]:
                counter += 1
                r += 1

        if counter == 1:
            dummy.append(chars[l])
        else:
            dummy.extend([chars[l]] + list(str(counter)))

        chars[:] = dummy
        return len(chars)
