import requests
from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup
import sys

# 5 song choices
AM1 = "http://www.lyrics.com/do-i-wanna-know-lyrics-arctic-monkeys.html"
AM2 = "http://www.lyrics.com/r-u-mine-lyrics-arctic-monkeys.html"
AM3 = "http://www.lyrics.com/arabella-lyrics-arctic-monkeys.html"
AM4 ="http://www.lyrics.com/whyd-you-only-call-me-when-youre-high-lyrics-arctic-monkeys.html"
mc=MarkovChain()


#  This section gets the html info from a lyric site.
def lyric_parse(song_link):
    r = requests.get(song_link)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

# This section pulls out the lyrics and puts into a list
def lyric_stripped(soup):
    rough=soup.find_all(itemprop='description')
    results = list(map(str, rough[0].contents))
    stripped_results = []
    for line in results[:-5]:
        if line != "<br/>":
            if line:
                stripped_results.append(line.strip())
    song =''.join(stripped_results)
    return song
    

print ("Would you like to see a new song from the Artic Monkeys?")
ans = input("yes(y)) or no(n)-  ")
if ans ==  "n":
    print ("Bye Bye!")
    sys.exit()
else:
    print ("Let's choose a song")

print("Which of the following do you like? (yes (y) or no (n) - ")
ans1 = input("Do I wanna know?- ")
if ans1 =="yes":
    mc.add_string(lyric_stripped(lyric_parse(AM1)))
else:
    pass
input("R U mine?- ")
if ans1 =="yes":
    mc.add_string(lyric_stripped(lyric_parse(AM2)))
else:
    pass
input ("Arabella?- ")
if ans1 =="yes":
    mc.add_string(lyric_stripped(lyric_parse(AM3)))
else:
    pass
input ("Why do you only call me when your are high?- ")
if ans1 =="yes":
    mc.add_string(lyric_stripped(lyric_parse(AM4)))
else:
    pass

print ("***  Here is the New song with more Cowbell!",)
x =mc.generate_text()
x = ' '.join(x)
print(x)







# Previous generator code that worked
# mc=MarkovChain()
# mc.add_string(song1)
# mc.add_string(song2)
# mc.add_string(song3)
# mc.add_string(song4)
# x =mc.generate_text()
# x = ' '.join(x)
# print(x)

#  Working code from before when doing one song at a time.
#r2 = requests.get('http://www.lyrics.com/r-u-mine-lyrics-arctic-monkeys.html')
#soup = BeautifulSoup(r2.content, "html.parser")

# This section pulls out the lyrics and puts into a list
#rough=soup.find_all(itemprop='description')
#results2 = list(map(str, rough[0].contents))
#stripped_results2 = []
#for line in results2[:-5]:
#    if line != "<br/>":
#        if line:
#            stripped_results2.append(line.strip())
#song2 =''.join(stripped_results2)



#  This section pulls out the breaks
# new_rough = rough.replace("<br/>", "")


# print(new_rough)

# This printed the lyrics but included div class and <br>  print(soup.find_all(itemprop='description'))
# This found null print(soup.find_all('lyrics'))
# from jerry.  Said worked on 2.7  --  print ("".join(map(str, div.contents)))
#div = soup.find('div', id='lyrics')
#soup = BeautifulSoup(r.content, builder=HTMLParserTreeBuilder())

#rough=soup.find_all(itemprop='description')
#print(''.join(map(str, rough[0].contents)))
# trying someting new --rough=str(soup.find_all(itemprop='description'))
