netctl的任务要激活 使用有2种方法
    systemctl enable netctl-auto@service_name
  另外一种方法
    netctl enable service_name
netctl list 列出全部的netctl service

wifi-menu will be available after netctl installed(dialog,dhcpcd is required)

iwd 包,配置文件在 /var/lib/iwd
iwctl

device list
device wlan0 set-property Powered on
station wlan0 scan
station wlan0 get-networks
station wlan0 connect SSID ;这里将会提问密码，至此设置完成

