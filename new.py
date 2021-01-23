one=input('Grade of subject #1:')
two=input('Grade of subject #2:')
three=input('Grade of subject #3:')
four=input('Grade of subject #4:')
five=input('Grade of subject #5:')

sum = 0

if one == "A" :
    sum += 4
elif one == "B" :
        sum += 3
elif one == "C" :
        sum += 2
elif one == "D" :
        sum += 1
elif one == "F" :
        sum += 0

if two == "A" :
    sum += 4
elif two == "B" :
        sum += 3
elif two == "C" :
        sum += 2
elif two == "D" :
        sum += 1
elif two == "F" :
        sum += 0

if three == "A" :
    sum += 4
elif three == "B" :
        sum += 3
elif three == "C" :
        sum += 2
elif three == "D" :
        sum += 1
elif three == "F" :
        sum += 0

if four == "A" :
    sum += 4
elif four == "B" :
        sum += 3
elif four == "C" :
        sum += 2
elif four == "D" :
        sum += 1
elif four == "F" :
        sum += 0

if five == "A" :
    sum += 4
elif five == "B" :
        sum += 3
elif five == "C" :
        sum += 2
elif five == "D" :
        sum += 1
elif five == "F" :
        sum += 0

Ans = sum/5
print(f"GPA : {Ans:.2f}")