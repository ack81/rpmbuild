#!/bin/bash
file=$1
newfile="cb-python-${file}"

echo '%global _python_bytecompile_errors_terminate_build 1' > $newfile
echo '%define debug_package %{nil}' >> $newfile
cat $file >> $newfile

# change global name variable
sed -ri 's/(^.define )(name)(.*$)/\1__\2\3/g' $newfile
sed -ri 's/\{name\}/\{__name\}/g' $newfile

# prepend cb-python to package name
sed -ri 's/(^Name: )(.*)$/\1cb-python-\2/g' $newfile

# delete orig file
rm -f $file

#build
rpmbuild -ba $newfile
