
from collections import namedtuple
from collections import Counter
from collections import defaultdict

c = Counter('aaaaabbbbbbbbbaaaaabbb')
print c
lst = [5,6,7,1,3,9,9,1,2,5,5,7,7]
c = Counter(lst)
print(c)

s = 'the lazy dog jumped over another lazy dog'
words = s.split()
print Counter(words).most_common(3)

fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
print guava
apple = fruit(number=5,variety='Granny Smith',color='red')
