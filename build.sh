#!/bin/bash -e

rm -rf Courses/__pycache__/
build_html/build_html.sh
build_tma/build_tma.sh
rsync -avz html/ tma_server:/mnt/lscode.me/dist/
