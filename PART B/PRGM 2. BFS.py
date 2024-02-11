from collections import defaultdict
jug1 = int(input("max capacity of jug1: "))
jug2 = int(input("max capacity of jug2: "))
goal = int(input("Enter capacity to be measured: "))
visited = defaultdict(lambda:False)

def waterjug(a1,a2):
  if(a1==goal and a2==0) or (a2==goal and a1==0):
    print(a1,a2)
    return True
  if visited[(a1,a2)] == False:
    print(a1,a2)
    visited[(a1,a2)] = True
    return (waterjug(0,a2) or waterjug(a1,0) or waterjug(jug1,a2) or waterjug(a1,jug2) or 
            waterjug(a1+min(a2,jug1-a1) , a2-min(a2,jug1-a1)) or waterjug(a1-min(a1,jug2-a2),a2+min(a1,jug2-a2)))
  else:
    return False

print('Steps: ')
waterjug(0,0)
