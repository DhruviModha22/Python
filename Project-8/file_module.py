def write_to_file(filename,content):
    with open(filename,'w')as f:
        f.write(content)


def read_from_file(filename):
    try:
        with open(filename,'r')as f:
            return f.read()
    except FileNotFoundError:
        return 'File not found'
    
def append_to_file(filename,content):
    try:
        with open(filename,'a')as f:
            f.write(content + '\n')
    except Exception as e:
        return str(e)