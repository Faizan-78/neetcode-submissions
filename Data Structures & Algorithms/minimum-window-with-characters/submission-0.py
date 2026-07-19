class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqT = {}
        window = {}

        for c in t:
            freqT[c] = freqT.get(c, 0) + 1

        have = 0
        need = len(freqT)

        resLen = float("inf")
        resL = 0

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in freqT and window[c] == freqT[c]:
                have += 1

            while have == need:

                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    resL = l

                window[s[l]] -= 1

                if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                    have -= 1

                l += 1

        if resLen == float("inf"):
            return ""

        return s[resL:resL + resLen]