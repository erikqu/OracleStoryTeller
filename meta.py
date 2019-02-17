from controller import main


def get_rest():
    text = "the user has gone wild, they are no longer responding." 
    rest = main(text)
    #rest = rest.pop()
    print(rest)
    return
get_rest()
