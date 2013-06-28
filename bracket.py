#-*- coding: cp1251 -*-
import sys
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
openbrackets = brackets.keys()
closebrackets = brackets.values()

def is_correct(a):
    step = []
    for c in a:
        if c in openbrackets:
            step.append(c)
        elif c in closebrackets:
            if step == []:
                return False
            x = step.pop()
            if brackets[x] != c:
                return False
    if step == []:
        return True
    else:
        return False

def main():
    for a in sys.argv[1:]:
        print a
        if is_correct(a):
            print "Yes"
        else:
            print "No"

if __name__=="__main__":
    main()
