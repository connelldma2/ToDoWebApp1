FILEPATH = "external.txt" # defining a GLOBAL CONSTANT

def show_list(list_arg):
    i = 1
    for item in list_arg:
        item = item.strip('\n')
        item = item.title()
        print('{}. {}'.format(i, item))
        i = i + 1

def get_file_todos(filepath=FILEPATH):
    """ Read a text file and return
    the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos

def write_file_todos(todo_list, filepath=FILEPATH):
    """ Write the to-do list to the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todo_list)


# test script
if __name__ == '__main__':
    print('This conditional IF BLOCK is used for script testing purposes.')