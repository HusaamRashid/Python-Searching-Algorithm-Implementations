#Insertion Sort
dataset = [5,3,1,7,11,33,0,-1]
def Insertion(data):
  for i in range(len(data)):
    current = data[i]
    pos = i - 1
    #checks if theres items to the left and then checks if the item to the left is greater than the current item
    while pos >= 0 and data[pos] > current:
      data[pos + 1] = data[pos]
      pos = pos - 1
    #once the loop has completed we have found the correct place
    #at which point we can place the item back in
    data[pos + 1] = current
  return data

sortedData = Insertion(dataset)
print(sortedData)