s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
Palindrome_List = []
Palindrome_temp_List = []
i = 0
j = len(s) - 1
a = 0
b = 1
k = 0
count = 0
while 1:
    if i == len(s) - 1:
        break
    if i == j:
        i = i + 1
        k = i
        j = len(s) - 1
    if s[i] == s[j] and i != len(s) - 1:
        Palindrome_temp_List.insert(a, s[i])
        Palindrome_temp_List.insert(b, s[j])
        a = a + 1
        b = b + 1
        i = i + 1
        j = j - 1
        count = count + 1
        if i == j:
            Palindrome_temp_List.insert(a, s[i])
            Palindrome_List.append(Palindrome_temp_List)
            a = 0
            b = 1
            Palindrome_temp_List = []
            i = k + 1
            k = i
            j = len(s) - 1
            count = 0
        if i > j:
            Palindrome_List.append(Palindrome_temp_List)
            a = 0
            b = 1
            Palindrome_temp_List = []
            i = k + 1
            k = i
            j = len(s) - 1
            count = 0
    if s[i] != s[j] and count == 0:
        i = k
        j = j - 1
        Palindrome_temp_List = []
        a = 0
        b = 1
    if s[i] != s[j] and count > 0:
        i = k
        j = j + (count - 1)
        Palindrome_temp_List = []
        a = 0
        b = 1
        count = 0
if Palindrome_List:
    print(''.join(max([(len(i), i) for i in Palindrome_List])[1]))
else:
    print('empty list')

    
        
        
                
