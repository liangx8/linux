devpath=`udevadm info --query=path --name=$1`
echo $devpath
udevadm info --attribute-walk --path=$devpath
