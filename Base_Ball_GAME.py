class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #T(C(N)==O(N)) and S(C(N)==O(N)) as it requires non contigous memory allocation iteratively
        st=[]#initlize stack
        for c in operations:#iterating through operational record 
            if c=='+':st.append(st[-1]+st[-2])#appending stack with prev record 
            elif c=='D':st.append(st[-1]*2)# doubleingthe prev's  Record and Appending it 
            elif c=='C':st.pop()#stack's element removal
            else:st.append(int(c))#appending the operational prev element
            
        return sum(st)#printing stack's sum
