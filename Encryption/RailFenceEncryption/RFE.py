def RFE(plain_text, level):
    plain_text = plain_text.replace(' ','') #removing white spaces from the plain_text
    cipher_text = [[] for i in range(level)] #creating a list which contains level number of list
	i = 0
    reverse = False 
    isWritten = False
	# below loop just append the alphabets in their respective list of levels and 
    for j in plain_text:
        cipher_text[i].append(j)
        isWritten = True
        if ( i == (level-1) and isWritten ):
            i = i-1
            isWritten = False
            reverse = True
        elif( i != 0 and isWritten ):
            if( reverse ):
                i = i - 1
                isWritten = False
            else:
                i = i + 1
                isWritten = False
        if( i == 0 and isWritten):
            i = i + 1
            isWritten = False
            reverse = False
   # now printing encrypted text
    for i in cipher_text:
       print("".join(i),end='')
