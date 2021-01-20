def input_user():
    """Prompt user to type input.
    
    :return: input by user.
    :rtype: str"""

    inp = input("\nPLease enter inegers separetad by space:\n")

    return inp
    

def process(inp):
    """Process integers."""

    list_of_inst = [int(x) for x in inp.split()]
    return sum(list_of_inst)


if __name__ == "__main__":

    process(input_user())
