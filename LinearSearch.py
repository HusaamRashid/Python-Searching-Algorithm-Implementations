data=['Antelope','Bat','Cheetah','Duck','Eel','Falcon','Guppy','Hamster','Jerboa','Koala','Mamba','Talon']

def LinearSearch(dataset, term): 
  for i in range(len(dataset)):
    if dataset[i] == term:
      return True
  return False
    
result = LinearSearch(data, 'Mamba')
print(result)

    
  
  