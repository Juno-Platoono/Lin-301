#!/bin/bash            
curl -o holmes.txt https://www.gutenberg.org/cache/epub/1661/pg1661.txt
mkdir backup_check               
echo "downloaded!"                              
mv holmes.txt backup_check                     