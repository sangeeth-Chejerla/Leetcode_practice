import collections

def uncommon_word(A,B):
    count = collections.Counter(A.split())
    count += collections.Counter(B.split())

    return [word for word in count if count[word]==1]

res = uncommon_word("this is just beginning","this is the ending")
print(res)




def uncommonFromSentences( s1: str, s2: str):
  s11 = s2
  s22 = s1
  words = s11.split()
  words2 = s22.split()
  ans = []
  freqDict = {}
  for w in words:
      freqDict[w] = freqDict.get(w,0)+1
  for w,v in freqDict.items():
      if v==1:
          if w not in words2:
              ans.append(w)
  
  words = s1.split()
  words2 = s2.split()
  
  freqDict = {}
  for w in words:
      freqDict[w] = freqDict.get(w,0)+1
  for w,v in freqDict.items():
      if v==1:
          if w not in words2:
              ans.append(w)
  return list(set(ans))
