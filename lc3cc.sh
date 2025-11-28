#!/bin/zsh

lc3as "./programs/$1.asm"
if [ $? -eq 0 ]; then
  echo "compiled lc3"
else 
  echo $?
  exit 1 
fi 

mv ./programs/*.obj ./bin/
mv ./programs/*.sym ./bin/ 

python memory_converter.py -i "./bin/$1.obj" -o "./memories/$1.hex"
