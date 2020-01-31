import sys
lst = __file__.split('/')
base_path  = '/'.join(lst[:-2])
sys.path.append(base_path)
from core import main

if __name__ == '__main__':
    main.entry_point()