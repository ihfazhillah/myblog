#!/bin/bash

generated_dir=$(realpath .)
echo "generated dir is " + $generated_dir
echo "copy it content into content folder"
cp $generated_dir/*.md $generated_dir/../content
echo "removing generated files"
rm -R $generated_dir
echo "operation succesfully.. :)"
