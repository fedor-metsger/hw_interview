
from stack import Stack

def main():
    braces = input()
    s = Stack()

    for i in range(len(braces)):
        if braces[i] in "([{": s.push(braces[i])
        elif braces[i] == ")" and s.pop() != "(" or \
                braces[i]  == "]" and s.pop() != "[" or \
                braces[i]  == "}" and s.pop() != "{":
            if s.pop() != "(":
                print("Несбалансировано")
                return

    print("Сбалансировано")





if __name__ == "__main__":
    main()