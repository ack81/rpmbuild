#!/bin/bash
file=$1
dir=$(echo $file | sed -rn 's/(.*)\.tar\.gz$/\1/p')

tar xzf $file
cd $dir

/opt/cb/bin/python setup.py bdist_rpm --packager="Adam Kinney <akinney@cloudbolt.io>" --python="/opt/cb/bin/python" --no-autoreq --spec-only --build-requires="cb-python" --dist-dir="/root/rpmbuild/SPECS"
