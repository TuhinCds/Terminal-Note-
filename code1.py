class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        obj = {
            "Q":1,"W":1,"E":1,"R":1,"T":1,"Y":1,"U":1,"I":1,"O":1,"P":1,"A":2,"S":2,"D":2,"F":2,"G":2,"H":2,"J":2,"K":2,"L":2,
            "Z":3,"X":3,"C":3,"V":3,"B":3,"N":3,"M":3
        }

        __STACK = []
        __MAIN_STACK = []
        for i in range(0, len(words)):
            stack__set = []
            for k in range(0, len(words[i])):
                if obj.get(words[i][k].upper()):
                    stack__set.append(obj.get((words[i][k]).upper()))
            __STACK.append(stack__set)
        for k in range(0, len(__STACK)):
            stack_sum = sum(__STACK[k])
            __arr__sum = len(__STACK[k]) * __STACK[k][0]
            if stack_sum == __arr__sum:
                __MAIN_STACK.append(words[k])

        return __MAIN_STACK


print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))