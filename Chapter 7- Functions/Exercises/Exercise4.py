def make_shirt(size='large', message='I love Python.'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It says, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('x-large', 'I am too tired')