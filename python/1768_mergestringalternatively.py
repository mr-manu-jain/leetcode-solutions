def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    for a,b in zip(word1,word2):
        merged.append(a+b)
    

    merged.append(word1[len(word2):])  
    merged.append(word2[len(word1):])

    print ("".join(merged))


mergeAlternately("abc","pqrstuv")