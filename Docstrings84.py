# Docstring to comment a function
# Add comment in the function to help users to understand the function
def tithing():
    """Info: This function calculate the tithing, exactly 10% of the value the user inputs."""
    x = float(input('Insert your salary: '))
    y = (x * 0.10)
    print(f'Tithing is $ {y} dollars.')

# Returns the comments in a function
help(tithing)
print(tithing.__doc__)



