tree = [None] * 100  # you can also initialise it with "" instead. 15 is the number of elements

global parent

def root(key):
    if tree[0] != None:
        print("Tree already had root")
    else:
        tree[0] = key


def set_left(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 1] = key


def set_right(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 2, ", no parent found")
    else:
        tree[(parent * 2) + 2] = key


def findelement(search):
    """"
    foundflag = False
    for i in range(len(tree)):
        if tree[i] == value:
            print(tree[i], i)
            foundflag = True
            break
    if foundflag == False:
        print("Value not in tree")
    """""
    global tree

    first = 0
    last = len(tree) - 1

    Found = False

    while first <= last and not Found:
        mid = (first + last) / 2

        mid = round(mid)
        print(str(tree[mid]))
        print(search)

        if str(tree[mid]) == search:
            Found = True
            print("Value found")
        else:
            if search < str(tree[mid]):
                last = mid - 1
            else:
                first = mid + 1

    if not Found:
        print("yup it aint in here")

def print_tree():  # change this to print in order traversal task 2.6
    for i in range(len(tree)):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()


# Driver Code inserting each of the nodes in the tree

root("Maroon")
set_right("Silver", 0)
set_left("Black", 0)
set_right("Indigo", 1)
set_left("Amber", 1)
set_right("Blue", 3)
set_right("Fuschia", 8)
set_right("Lime green", 4)
set_left("Grey", 4)
set_left("Red", 2)
set_right("Violet", 2)
set_left("Pink", 5)
set_right("Purple", 11)
set_left("Turquoise", 6)
set_right("Yellow", 6)
print_tree()
findelement("Red")
