import sys
filename = sys.argv[1]
text = open(filename, 'rb').read().replace('\r\n', '\n')
open(filename, 'wb').write(text)