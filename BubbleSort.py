dataset = [0,1,2,18,4,7,6,11,8,9,5,3]

def bubblesort(data):
  for i in range(0, len(data)):
    for i in range(0,len(data) - 1):
      if data[i] > data[i+1]:
        placeholder = data[i]
        data[i] = data[i+1]
        data[i+1] = placeholder
    
  return data


print(bubblesort(dataset))

def insertionSort(data):
  
  
  