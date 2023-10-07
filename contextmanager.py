from contextlib import contextmanager
@contextmanager
def open_managed_file(filename):
    f=open(filename,'w')
    try:
        f.write("some thing...")
        yield f
    finally:
        f.close()
        
open_managed_file("note.txt")            