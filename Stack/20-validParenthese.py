class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        #stack : LIFO => avec .pop, on ajoute et retire toujours sur la droite
        stk = []

        for c in s:
            #c représente les clés du dict. => c not in hashmap == opening bracket
            if c not in hashmap:
                stk.append(c)
            else:
                #si pile vide
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    #c is the closing bracket
                    if popped != hashmap[c]:
                        return False
        #inversion de la liste booléenne
        return not stk
    #time : O(n), Space : O(n)