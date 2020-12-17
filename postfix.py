
# modul obsahuje funkcie zodpovedajúce operáciám

import operator

# slovník operácie → funkcie dvoch premenných
op_name={
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.floordiv,
    }

def eval_expr(s,d={}):

    stack=[]
    for word in s.split():
        if word in ("+","*","-","/"):
           a=stack.pop()
           b=stack.pop()
           stack.append(op_name[word](b,a))
        elif word in d:
            stack.append(d[word])
        else:
            stack.append(int(word))
    return stack.pop()

def to_infix(s):

    stack=[]
    for word in s.split():
        if word in ("+","*","-","/"):
           a=stack.pop()
           b=stack.pop()
           stack.append("( %s %s %s )" % (b,word,a))
        else:
            stack.append(word)
    return stack.pop()

def to_postfix(s):

    stack=[]
    ret_l=[]
    for word in s.split():
        if word=="(":
            continue
        if word in ('+','-','*','/'):
            stack.append(word)
        elif word==")":
            ret_l.append(stack.pop())
        else:
            ret_l.append(word)
    return " ".join(ret_l)

# Toto je trik: kód za podmienkou sa vykoná iba
# pri spustení ako skript, nie pri importe.
# Takto môžem v kóde nechať pomocné výpisy.
if __name__=="__main__":
    print(eval_expr("10 2 + 3 *"))
    print(eval_expr("1 2 * 3 +"))
    print(eval_expr("1 2 /"))
    print(eval_expr("2 1 /"))
    print(eval_expr("2 x /",{'x':2}))
    print(to_infix("1 2 + 3 *"))
    print(to_infix("10 2 4 * 3 - /"))
    print(to_postfix(to_infix("10 2 4 * 3 - /")))
    print(to_postfix(to_infix("1 2 + 4 * 3 - 5 /")))


