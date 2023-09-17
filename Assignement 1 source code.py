#Qn 1
x=2.5
y=3
f=2**(x+y) + 3*x**y + (2*y)**x
print('f=%f'%f)
print()

#Qn 2
import math

initial_N =float(input('Enter N_0 value:'))
print('For initial N value = %0.3f' %initial_N)
print('t=0, N=%0.3f' %initial_N) #print values for t=0

t= int(input('Enter values of t from 1 to 4:')) #to compute N values for t=1,2,3,4
N = initial_N * (math.exp(t*-1)) #compute N
percentage_loss = ((initial_N - N) / initial_N) * 100 #compute percentage loss
print('t=%d, N=%0.3f, loss=%0.2f%%' %(t,N,percentage_loss)) #print values

t= int(input('Enter values of t from 1 to 4:'))
N = initial_N * (math.exp(t*-1))
percentage_loss = ((initial_N - N) / initial_N) * 100
print('t=%d, N=%0.3f, loss=%0.2f%%' %(t,N,percentage_loss))

t= int(input('Enter values of t from 1 to 4:'))
N = initial_N * (math.exp(t*-1))
percentage_loss = ((initial_N - N) / initial_N) * 100
print('t=%d, N=%0.3f, loss=%0.2f%%' %(t,N,percentage_loss))

t= int(input('Enter values of t from 1 to 4:'))
N = initial_N * (math.exp(t*-1))
percentage_loss = ((initial_N - N) / initial_N) * 100
print('t=%d, N=%0.3f, loss=%0.2f%%' %(t,N,percentage_loss))
print('\nEnd')

#Qn 3
test1='PYTHON IS MY FAVORITE PROGRAMMING LANGUAGE'
print('The test string is: %s' %test1)
print('a. The first five characters are:',test1[:5])
print('b. The last three characters are:',test1[-3:])
print('c. The even characters are:',test1[::2])
print('d. The last five characters in reverse order:',test1[:-6:-1])

test2='This is the first lab assignment for TIE2030.'
print('\nThe test string is: %s' %test2)
print('a. The first five characters are:',test2[:5])
print('b. The last three characters are:',test2[-3:])
print('c. The even characters are:',test2[::2])
print('d. The last five characters in reverse order:',test2[:-6:-1])

test3='My code finally works!!!'
print('\nThe test string is: %s' %test3)
print('a. The first five characters are:',test3[:5])
print('b. The last three characters are:',test3[-3:])
print('c. The even characters are:',test3[::2])
print('d. The last five characters in reverse order:',test3[:-6:-1])
print()

#Qn 4
test1='PYTHON IS MY FAVORITE PROGRAMMING LANGUAGE'
print('The test string is: %s' %test1)
print('a. The number of characters in the sentence:',len(test1))
print('b. The first index of the space character:',test1.index(' '))
print('c. Replacing space with -:',test1.replace(' ','-'))
print('d. All characters in upper case:',test1.upper())

test2='This is the first lab assignment for TIE2030.'
print('\nThe test string is: %s' %test2)
print('a. The number of characters in the sentence:',len(test2))
print('b. The first index of the space character:',test2.index(' '))
print('c. Replacing space with -:',test2.replace(' ','-'))
print('d. All characters in upper case:',test2.upper())

test3='My code finally works!!!'
print('\nThe test string is: %s' %test3)
print('a. The number of characters in the sentence:',len(test3))
print('b. The first index of the space character:',test3.index(' '))
print('c. Replacing space with -:',test3.replace(' ','-'))
print('d. All characters in upper case:',test3.upper())
print()

#Qn 5
word=input('Please input a 5 alphabet word: ')
word_list=[word[0],word[1],word[2],word[3],word[4]]
print(word_list)
print()

#Qn 6
tuple1=()
print('a.Type of tuple:', type(tuple1))
print('a.Empty tuple:', tuple1)

tuple1=(-2, 4, -7, 29, 17, 0, 101, 8, 9, 21, 6, 15, 28, -100)
print('b.The new tuple is:', tuple1)
print('c.Number of items in the tuple:', len(tuple1))
print('d.Last item in the tuple:', tuple1[-1])
print('e.Elements from 3rd to 9th elements:',tuple1[2:9])
print('f.Max value in the tuple:',max(tuple1))
print('f.Min value in the tuple:',min(tuple1))
print('g.Index of max value in the tuple:',tuple1.index(max(tuple1)))
print('g.Index of min value in the tuple:',tuple1.index(min(tuple1)))

convert_tuple1=list(tuple1)
convert_tuple1[0]=100
tuple1=tuple(convert_tuple1)
print('h.Tuple with replaced 1st element:',tuple1)
print()
