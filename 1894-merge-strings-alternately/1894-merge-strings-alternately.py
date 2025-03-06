class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A,B= len(word1), len(word2)
        a,b = 0,0
        merge=[]

        word=1
        while a<A and b<B:
            if word==1:
                merge.append(word1[a])
                a += 1
                word = 2
            else:
                merge.append(word2[b])
                b +=1
                word = 1
        
        while a<A:
            merge.append(word1[a])
            a += 1
        while b<B:
            merge.append(word2[b])
            b += 1

        return ''.join(merge)


        
        