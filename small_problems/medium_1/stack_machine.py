POP_COMMANDS = ['ADD', 'SUB', 'MULT', 'DIV', 'REMAINDER', 'POP']

def stack_empty(stack):
    if stack:
        return False
    return True

def valid_number(string):
    if (string[0] == '-' and string[1:].isdigit()) or string.isdigit():
        return True
    return False
    

def minilang(commands):
    register = 0
    stack = []

    for command in commands.split():
        if command in POP_COMMANDS and stack_empty(stack):
            print('ERROR: Stack is empty.')
            return None
        
        match command:
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()
            case 'POP':
                register = stack.pop()
            case 'PRINT':
                print(register)
            case _:
                if not valid_number(command):
                    print(f'Invalid command: {command}')
                    return None
                register = int(command)

minilang('5 PUSH -3SQUASH3 PRINT')
# Invalid command: -3SQUASH3

minilang('POP')
# ERROR: Stack is empty.

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)