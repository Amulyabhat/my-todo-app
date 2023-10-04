FILEPATH= 'Files/todos.txt'


def get_todos(filep=FILEPATH):
    """Read a text file and open it """
    with open(filep, 'r') as filel:
        todosl = filel.readlines()
    return todosl

def write_todos(todosarg, filep=FILEPATH):
    """Write and output the text file"""
    with open(filep, 'w') as filel:
        filel.writelines(todosarg)

print(__name__)
if __name__=="__main__":
    print("hello")
    print(get_todos())
