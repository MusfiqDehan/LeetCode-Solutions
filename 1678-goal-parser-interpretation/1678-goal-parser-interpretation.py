# class Solution:
#     def interpret(self, command: str) -> str:
#         return command.replace('()','o').replace('(al)','al')

import re
class Solution:
    def interpret(self, command: str) -> str:
        return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))
        