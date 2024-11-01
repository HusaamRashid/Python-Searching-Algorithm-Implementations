#Binary Search
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def binarySearch(data, term):
  bot = 0
  top = len(data) - 1
  while bot <= top:
    mid = (bot + top) // 2
    print(data[mid])
    if data[mid] == term:
      return True
    elif data[mid] < term:
      bot = mid + 1
    else:
      top = mid - 1
  return False
      


result = binarySearch(data,9)
print(result)
    
  
    
  