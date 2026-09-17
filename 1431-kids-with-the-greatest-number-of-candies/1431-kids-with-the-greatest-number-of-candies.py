class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lst=[True]*len(candies)
        for i in range(len(candies)):
            x=candies[i]+extraCandies
            if i==0:
                for j in range(i+1,len(candies)):
                    if x<candies[j]:
                        lst[i]=False
                        break
            elif i==len(candies)-1:
                for j in range(i-1,-1,-1):
                    if x<candies[j]:
                        lst[i]=False
                        break
            else:
                for j in range(i+1,len(candies)):
                    if x<candies[j]:
                        lst[i]=False
                        break
                for j in range(i-1,-1,-1):
                    if x<candies[j]:
                        lst[i]=False
                        break
        return lst
                

                        
                    
                    


