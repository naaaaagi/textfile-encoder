import sys
import os

path = sys.argv[1]

import_encoding = input("import encoding: ")

with open(path, encoding=import_encoding) as f:
    contents = f.read()
    print(contents)

export_encoding = input("export encoding: ")
export_path = f'{os.path.splitext(path)[0]}[{export_encoding}]{os.path.splitext(path)[1]}'
print(export_path)

with open(export_path, mode='w', encoding=export_encoding) as f:
    f.write(contents)
