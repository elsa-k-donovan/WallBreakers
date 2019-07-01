class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        
        #defining a dictionary [key: letters, values: morse code]
        morse = {'a': ".-",'b': "-...",'c': "-.-.", 'd': "-..",'e': ".",'f': "..-.",'g': "--.",'h': "....",'i': "..",'j': ".---",'k': "-.-",'l': ".-..",'m': "--",'n': "-.",'o': "---",'p': ".--.",'q': "--.-",'r': ".-.",'s': "...",'t': "-",'u': "..-",'v': "...-",'w': ".--",'x': "-..-",'y': "-.--",'z': "--.."}
        
        #initialize set
        setResults = set()
        
        #translate words to morse code
        for x in words:
            result =""
            x = list(x)
            for i in x:
                result += morse[i]
            setResults.add(result)
            
        #return number of transformations
        transformations = len(setResults)
        return transformations
