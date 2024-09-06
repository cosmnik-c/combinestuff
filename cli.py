import internal
import os

debug = False

def log(*args, joiner = ' '):
    '''output *args with joiner as seperator if debug mode is true
example: log(2,3,5,joiner = '[') #2[3[5'''
    if debug:
        print(joiner.join([str(i) for i in args]))

def clear():
    '''clear terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')

#read save
with open("./unlocked.txt",'r') as unlocked_file:
    unlocked = set(unlocked_file.read().split(';'))


#read recipes (i should comment the code but i barely understand what i made)
#recipes are seperated by newlines and are in the format item1 + item2 + item3 + ... > result1 + result2 +...
#for example water + fire > steam
#use # at beginning of line to comment
with open("./recipes.txt") as r:
    recipes = internal.load_recipe(r)


a = internal.Game(recipes, unlocked, './unlocked.txt')
print('type exit to exit and save progress\nreset to reset progress(you will have to restart app)\ncommands in format item1+item2+item3+... without spaces')
while True:
    print('what you have:', ', '.join(a.unlocked))
    inp = input()
    if inp == 'exit':
        a.save()
        break
    elif inp == 'reset':
        a.save('earth;fire;water;air')
        break
    else:
        clear()
        out = a.combine([i.strip() for i in inp.split('+')])
        if   out[0] == 'already made':
            print(f'you made {", ".join(out[1])} but you already had it.')
        elif out[0] == 'made':
            print(f'you made {", ".join(out[1])}!')
        elif out[0] == 'no result':
            print('you didnt make anything.')
        elif out[0] == 'item unavailable':
            print(f'you dont have {", ".join(out[1])}!')
