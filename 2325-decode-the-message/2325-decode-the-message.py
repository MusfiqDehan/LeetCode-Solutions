class Solution:
    def decodeMessage(self, key, message):
        sub = dict()
        for k in key:
            if k.islower() and k not in sub:
                sub[k] = chr(ord('a')+len(sub))
        sub[' '] = ' '

        return ''.join( sub[m] for m in message )
        