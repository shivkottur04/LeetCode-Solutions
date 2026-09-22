class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace(",", " ").replace(";", " ").replace(".", " ").replace("'", " ")
        paragraph=paragraph.split()
        d={}
        for i in paragraph:
            if i not in banned:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        for key in d.keys():
            return key