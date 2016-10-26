#!/bin/sh

#sed -n '2,5p' filename

text1=$1
text2=$2

if [[ -z "${text1}" || -z "${text2}" ]];then
	echo "usage : $0 filename1 filename2"
	exit 255
fi

if [ ! -e "${text1}" ];then
	echo "${text1}: No such file"
	exit 255
fi

if [ ! -e "${text2}" ];then
	echo "${text2}: No such file"
	exit 255
fi

RED='\033[0;31m'
NC='\033[0m' # No Color

x=0
while read file1_line;do
	x=$(( x+1 ))
	file2_line=$(sed -n "${x}p" ${text2})
	if [[ "${file1_line}" == "${file2_line}" ]];then
		echo -e " [$file1_line] [$file2_line]"
	else
		echo -e "${RED}*[$file1_line] [$file2_line]${NC}"
	fi
done<${text1}

exit 0
