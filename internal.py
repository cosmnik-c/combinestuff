

#read recipes (i should comment the code but i barely understand what i made)
#recipes are seperated by newlines and are in the format item1 + item2 + item3 + ... > result1 + result2 +...
#for example water + fire > steam
#use # at beginning of line to comment
def load_recipe(recipe_file):
    recipes = {}
    for line in recipe_file.read().strip().split('\n'):
        if line.strip() != '':
            if line.strip()[0] == '#':
                continue
            splitline = line.split('>')
            if len(splitline) == 2:
                recipe = splitline[0].split('+')
                recipe = [item.strip() for item in recipe]
                recipedict = {}
                for i in recipe:
                    try:
                        recipedict[i] = recipedict[i] + 1
                    except:
                        recipedict[i] = 1
                recipe = set()
                for key, value in recipedict.items():
                    recipe.add((key, value))
                recipe = frozenset(recipe)
                result = [item.strip() for item in splitline[1].split('+')]
                recipes[recipe] = result
                #print(recipe, recipes[recipe])
    return recipes


class Game:
    def __init__(self, recipedict, unlocked, savefilename):
        self.recipes = recipedict
        self.unlocked = unlocked
        self.savefilename = savefilename
        self.debug = False
        

    def combine(self, itemlist):
        self.valid = True
        self.itemdict = {}

        for i in itemlist:
            try:
                self.itemdict[i] = self.itemdict[i] + 1
            except:
                self.itemdict[i] = 1

        #check if user actually has the items necessary
        itemset_unobtained = set()
        for key, value in self.itemdict.items():
            if not key in self.unlocked:
                itemset_unobtained.add(key)
                self.valid = False

        self.itemset = set()
        for key, value in self.itemdict.items():
            self.itemset.add((key, value))
        self.itemset = frozenset(self.itemset)

        self.log(self.itemset)
        
        if self.valid:
            #add result to unlocked if recipe exists
            try:
                self.result = self.recipes[self.itemset]
                for i in self.result:
                    self.unlocked.add(i)
                return ('made', self.result)
            except:
                return tuple('no result')
        else:
            return tuple(['item unavailable',itemset_unobtained])

    def log(self, *args, joiner = ' '):
        '''output *args with joiner as seperator if debug mode is true
example: log(2,3,5,joiner = '[') #2[3[5'''
        if self.debug:
            print(joiner.join([str(i) for i in args]))

    def save(self, save = None):
        '''saves'''
        with open(self.savefilename, "w") as unlocked_file:
            unlocked_file.write(';'.join(self.unlocked) if save == None else save)
                


            
            
