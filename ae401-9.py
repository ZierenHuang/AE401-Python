fo =  open('TPA.txt','a' )

switch = 'y'
while switch == 'y':
    n = input('what your name?')
    s = float(input('scores?'))
    fo.write(n +''+str(s)+'/n')
    switch = input('continue print y')
    
fo.close()

    