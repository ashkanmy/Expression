# Here, member-list of a class Variable that is called as self.tree plays the role of a stack.
class Variable:
        def __init__(self,value,tree=[]):
                self.value = value
                self.tree =tree
                #print(self.tree)
                #print('z.value -> ',self.value)
                #if (len(self.tree)>3):
                        #ln = len(self.tree)
                        #print(ln,ln/2) 
                        #print('->',self.tree[ln+1])
                        #print('->',self.tree[ln+2])
        def __add__(self,otherVariable):
                self.tree.append(str(self.value)) 
                self.tree.append(str(otherVariable.value)) 
                self.tree.append('ADD') 
                return Variable(self.value+otherVariable.value,self.tree)
        def __mul__(self,otherVariable):
                self.tree.append(str(self.value)) 
                self.tree.append(str(otherVariable.value)) 
                self.tree.append('MULT') 
                return Variable(self.value*otherVariable.value,self.tree)
        def __sub__(self,otherVariable):
                self.tree.append(str(self.value)) 
                self.tree.append(str(otherVariable.value)) 
                self.tree.append('SUB') 
                return Variable(self.value-otherVariable.value,self.tree)
        def __str__(self):
                cntr = -1 
                removingIndices = []
                ln = len(self.tree)
                for el in self.tree:
                        cntr+=1
                        if ((self.tree[cntr] == 'ADD' or self.tree[cntr] == 'MULT') and (cntr>=2 and cntr<ln-1)):
                                #print(el)
                                if self.tree[cntr]=='ADD' and int(self.tree[cntr-2])+int(self.tree[cntr-1]) == int(self.tree[cntr+1]):
                                        removingIndices.append(cntr+1)      
                                elif self.tree[cntr]=='ADD' and int(self.tree[cntr-2])+int(self.tree[cntr-1]) == int(self.tree[cntr+2]):
                                        removingIndices.append(cntr+2)      
                                if self.tree[cntr]=='MULT' and int(self.tree[cntr-2])*int(self.tree[cntr-1]) == int(self.tree[cntr+1]):
                                        removingIndices.append(cntr+1)      
                                elif self.tree[cntr]=='MULT' and int(self.tree[cntr-2])*int(self.tree[cntr-1]) == int(self.tree[cntr+2]):
                                        removingIndices.append(cntr+2)      
                #print(removingIndices)
                for ri in range(len(removingIndices)):
                        #self.tree[removingIndices[ri]]='-1'
                        self.tree[removingIndices[ri]]=self.tree[removingIndices[ri]]
                #print(self.tree)
                return('')
        def newTree(self):
                theStack=[]
                self.tree=list(reversed(self.tree)) 
                print('-- stack -->',self.tree)
                cntr = len(self.tree)-3
                while cntr>=0:
                        tRoot=self.tree[cntr]
                        tLeft=self.tree[cntr+1]
                        tRigh=self.tree[cntr+2]
                        #print(tLeft,'->',tRoot,'<-',tRigh)
                        #
                        if tRoot=='MULT':
                               if tLeft!='-1' and tRigh!='-1':
                                       theStack.append(str(int(tLeft)*int(tRigh)))
                               elif tLeft=='-1':
                                       tPopLeft=theStack.pop()
                                       theStack.append(str(int(tPopLeft)*int(tRigh)))
                               elif tRigh=='-1':
                                       tPopRigh=theStack.pop()
                                       theStack.append(str(int(tLeft)*int(tPopRigh)))
                        elif tRoot=='ADD':
                               if tLeft!='-1' and tRigh!='-1':
                                       theStack.append(str(int(tLeft)+int(tRigh)))
                               elif tLeft=='-1':
                                       tPopLeft=theStack.pop()
                                       theStack.append(str(int(tPopLeft)+int(tRigh)))
                               elif tRigh=='-1':
                                       tPopRigh=theStack.pop()
                                       theStack.append(str(int(tLeft)+int(tPopRigh)))
                        cntr-=3
                        #print('Result -> ',theStack)



