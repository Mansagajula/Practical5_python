fh=open('output5.txt','w')
a=int(input('Enter year: '))
if(a%4==0):
    print('It is a leap year')
    fh.write(f'{a} is a leap year')
else:
    print('Not a leap year')
    fh.write(f'{a} is not a leap year')
fh.close()
