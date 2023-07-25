#!/bin/bash

rm -rf media

manim -pql ${1}.py ${1}

dd=`ls /home/santosg/Python_Manim/media/videos/${1}/`
pati="/home/santosg/Python_Manim/media/videos/${1}/${dd}"

./mv1.sh ${1} ${pati}





