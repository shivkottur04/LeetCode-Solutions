class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if list1[i] not in d.keys():
                        d[list1[i]]=i+j
                        break
        result=[]
        for key,val in d.items():
            if d[key]==min(d.values()):
                result.append(key)
        return result
         

        