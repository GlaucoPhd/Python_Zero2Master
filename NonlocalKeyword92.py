# Start With Local
# Parent Local?
# Global

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nolocal'
        print('inner', x)

    inner()
    print('Outer:', x)

outer()

