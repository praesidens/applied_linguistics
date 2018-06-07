from operator import itemgetter
from timeit import default_timer as timer
from nltk.corpus import wordnet as wn


start = timer()

with open('friends_s1.txt', encoding='utf8') as file:
    text = file.readlines()
    words = []
    words += [word.strip("[].,...!?()«»:;\"")
              for line in text
              for word in line.split()
              if word.lower() not in ['rachel:', 'rachel',
                                      'ross:', 'ross',
                                      'monica:', 'monica', ' monica: ', 'monica: ',
                                      'chandler:', 'chandler',
                                      'joey:', 'joey',
                                      'phoebe:', 'phoebe',
                                      'end']]
print(len(words))

freq_dict = {}

for word in words:
    freq_dict[word] = freq_dict.get(word, 0) + 1

freq_dict = sorted(freq_dict.items(), key=itemgetter(1), reverse=True)

print(freq_dict)
top_freq = []
top_freq_sentences = []
i = 0
j = 1
sum_of_top_200 = 0
length = len(freq_dict)

while i < length and i < 500:
    sum_of_top_200 += freq_dict[i][1]
    i += 1

i = 0

while i < length and i < 500:
    for s in text:
        if freq_dict[i][0] in s and j > 0:
            try:
                top_freq_sentences.append(wn.morphy(freq_dict[i][0])
                                          + '\t'
                                          + str(freq_dict[i][1])
                                          + '\t'
                                          + s.strip("[].,...?()«»:;\"\n\t")
                                          + '.')
                break
            except TypeError:
                top_freq_sentences.append(freq_dict[i][0]
                                          + '\t'
                                          + str(freq_dict[i][1])
                                          + '\t'
                                          + s.strip("[].,... !?()«»:;\"\n\t")
                                          + '.')

            j -= 1
    i += 1
    j = 1

end = timer()
print('\n', end-start)
print(*top_freq_sentences, sep='\n')

print("SUM OF TOP-200", sum_of_top_200)