#!/bin/sh
cython --gdb app.pyx
python2 setup.py build_ext --inplace
rm -r build
rm app.c
