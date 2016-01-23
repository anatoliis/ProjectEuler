#!/bin/bash
python2 -m cProfile -s time -o output.prof "$1"
snakeviz output.prof