class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for x in range (1, n+1):
            if ((x % 3 == 0) and (x % 5 == 0)):
                result.append("FizzBuzz")
            elif x % 3 == 0:
                result.append("Fizz")
            elif x % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(x))
                
        return result

        
        #for i in range(1,n+1):
          #  result.append(str(i))
        
      #  for x in result:
          #  if eval(x) % 3 == 0:
           #     num = eval(x)
           #     fizz = "Fizz"
           #     result.insert(num, fizz) 
          #  elif int(x) % 5 == 0:
           #     x = "Buzz"
            
        
       # strin = [str(t) for t in result]
        
      #  return strin
        
        
       # for i in result:
          #  if i % 3 == 0:
         #       i = 'fizz'
       #     elif i % 5 == 0:
       #         i = 'buzz'
       #     else:
       #        i = str(i)
         #   result.append(i)
      
    
     #   print(result)
