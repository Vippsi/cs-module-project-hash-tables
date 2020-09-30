def no_dups(s):
    # Your code here
    # set up variable to hold new string
    new_string=''
    s = s.split()

    for w in s:
        if w not in new_string:
            if new_string == "":
                new_string += w
            else:
                new_string += f" {w}"
        else:
            continue
    return new_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))