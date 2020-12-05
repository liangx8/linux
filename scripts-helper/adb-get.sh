#!/bin/sh

# 从手机拉整个目录
ADB=/home/user/Android/Sdk/platform-tools/adb
# 要把字串中的\去掉
base=`echo $1|tr -d \\`
files=`$ADB shell ls /sdcard/$1`

for file in ${files[@]}
do
	full="/sdcard/$base/$file"
	echo -e "$ADB pull $full"
	$ADB pull "${full}"
done

