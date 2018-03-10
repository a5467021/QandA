#! /usr/bin/python3

import os


file = os.listdir();
a = 1;
for item in file:
    if os.path.isfile(item) and item.split('.')[-1] == 'jpg':
        os.rename(item, '{0}.jpg'.format(a));
        a += 1;
