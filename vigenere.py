whole="VMCOMGTVPULAUBKUDAOYIPYWVQFZFZNJMGXCPCJQGMRWBAZUYVEBLEYKVAEWDMTVPUSXZEFFKAFGERHXJUUFEEUDKZFMIMAZVLCIB"
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keylength = 7
frequency=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

key = ""
for h in range(keylength):
    string = ""
    for k in range(h,len(whole)-1,keylength):
        string = string + whole[k]
    found = []
    for char in chars:
        found.append(string.count(char)/len(string))

    values = []
    for j in range(len(frequency)):
        value = 0
        for i in range(len(frequency)):
            value = value + (frequency[i]*found[i])
        values.append(value)
        found.append(found.pop(0))
    key = key + chars[values.index(max(values))]
print(key)
