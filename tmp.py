#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
def main():
    p = subprocess.Popen("./tmp.sh 'param'", shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read()
    print out
    result = out.split()
    print result
    return 0

if __name__ == '__main__':
	main()
