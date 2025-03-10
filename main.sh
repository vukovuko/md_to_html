#!/bin/bash

python3 src/main.py "/md_to_html/"
cd docs && python3 -m http.server 8888