# word = new york
# word --> [(doc,postion)]

word1 = [(1,11), (1,16), (1,20), (2,50), (3,16)]  # new
word2 = [(1,90), (3,17)]  # york

from collections import defaultdict

word1_docs = defaultdict(list)
word2_docs = defaultdict(list)

for doc,pos in word1:
    word1_docs[doc].append(pos)

print(f"word1_docs : {word1_docs}")    
    
for doc,pos in word2:
    word2_docs[doc].append(pos) 

print(f"word2_docs : {word2_docs}")     

all_docs = set(word1_docs) | set(word2_docs)
print(f"all_docs : {all_docs}")

both_docs = []
phrased_docs = []
single_doc = []
    
for doc in all_docs:
    
    i = 0
    j = 0
    
    if doc in word1_docs and doc in word2_docs:
        is_phrase = False
        w1 = word1_docs[doc]
        w2 = word2_docs[doc]
        while i < len(w1) and j<len(w2):
            if w2[j]== w1[i]+1:
                is_phrase = True
                phrased_docs.append(doc)
                break
            elif w1[i] < w2[j]:
                i+=1
            else:
                j+=1
                
        if not is_phrase:
            both_docs.append(doc)
            
    else:
        single_doc.append(doc)

final_ranking = phrased_docs + both_docs + single_doc

print(final_ranking)
    
    
