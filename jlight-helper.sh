#!/bin/bash

gpio mode 0 out
mode=$(gpio read 0)
#echo $mode
if [ $mode -eq 1 ]; then
  gpio write 0 0
elif [ $mode -eq 0 ]; then
  gpio write 0 1
fi
