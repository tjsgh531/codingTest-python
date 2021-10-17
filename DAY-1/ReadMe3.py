# 정규표현식
import re

# match()
print(re.match('a','aa'))
print(re.match('a','leesunhoAa'))

#search()
print(re.search('a','what is that?'))

#findall()
print(re.findall('aa','where is aa in this sentence? aa'))
print(re.findall('\d','let\'s find 123number 12'))
print(re.findall('\d+', 'what happen this order 123 or 543 in its on'))

#fullmatch()
print(re.fullmatch('\d','1234567'))
print(re.fullmatch('\d+', '1234556'))
print(re.fullmatch('the', 'the'))

#split()
print(re.split('\.', 'ho.yo.we.ca.sj.lladi..di...dke'))
print(re.split('o','wow i am on a baot'))

#sub() == replaceAll()
print(re.sub('a','k','what is point a apple'))

#subn()
print(re.subn('a','k','what is point a apple'))

#compile()
temp = re.compile('a')
print(temp.sub('wowo', 'aaappellaa'))
print(re.sub('a','wowo','aaappleaa'))

#purge()
re.purge()

#group()/start()/end()
print(re.search('\d+','010.2041.2394').group())
