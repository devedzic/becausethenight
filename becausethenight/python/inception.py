# The code moved here from the initial version of main.py and improved with   if __name__ == "__main__":

def print_it():
    print("Because the Night")
    print()
    print('Because the night ' + '\n' + 'belongs to lovers')

'''
The following code is commented out, because it executes when print_it() is called from main.py. 
That happens because, by default, an imported module is run as a script.  
'''
# print_it()
# print()
#
# for i in range(1, 5):
#     print(i, " Because the Night")

if __name__ == "__main__":
    print_it()
    print()

    for i in range(1, 5):
        print(i, "Because the Night")       # no ' ' before 'B', it is now inserted automatically
    print()

    print('Because ', end='')               # end='...' avoids the newline after the output
    print("the Night")
    print()

    print('%6.2f, %5d' %(4/3, 2))
    print()

    title = 'Because the Night'
    a = input('Enter the year of release of ' + title + ': ')
    print(title, 'was first released in', a)

