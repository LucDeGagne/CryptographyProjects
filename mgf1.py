output = "" #Start with an empty output string

x = 2**7+2**9+2**10 #Our initial value = 1664
b = bin(x).replace("0b","") #Convert it to binary
while len(b) < 16:
    b = '0' + b #Ensure the value occupies two octets AKA 16 spaces
counter = 0 #Out counter is at 0
while len(output) < 40: #Because size is 5 octets and 8*5 = 40
    c = bin(counter).replace("0b","") #Take the counter from 0 to whater and make it binary
    while len(c) < 32:
        c = '0' + c #Make the counter the length of 4 octets where 8*4 = 32. This is where that magic number was. It's a standard number we don't need to change
    concat= b + c #Concatenate the values of the number and counter bin, making sure counter is the back end
    num = int(concat,2) #Convert it to a decimal number to run the "hash"
    hs = (2*num + 1)%65521 #Run the hash
    b = bin(hs).replace("0b","") #Convert BACK to a binary value
    while len(b) < 16:
        b = '0' + b #Convert it to 2 octets because the "output" always occupies to octets according to the assignment Q
    output = output + b #Concatenate this to the output
    counter = counter + 1 #Increment the counter

answer = output[:40] #Once the length is greater than 40 we just cut it off at our size which is 5 octets so 8*5 = 40
print(answer) #The binary answer
print(int(answer,2)) #The number is represents in decimal
print(hex(int(answer,2))) #The hex code (NOTE it's length is 10 AKA 5 octets)
