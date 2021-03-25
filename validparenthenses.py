

s = "()("
expected = ""
iterate_expected = -1
matching_dict = {"(": ")", "[": "]", "{": "}"}
if s.startswith(('(', '[', '{')):
    for i in range(0, len(s)):
        if s[i] in "([{":
            expected = expected + matching_dict[s[i]]
            iterate_expected = iterate_expected + 1
        else:
            if iterate_expected > -1 and s[i] == expected[iterate_expected]:
                expected = expected[:-1]
                iterate_expected = iterate_expected - 1
            else:
                print("False")
                exit()
    if len(expected) == 0:
        print("True")
    else:
        print("False")
else:
    print('False')