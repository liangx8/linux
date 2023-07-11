xorg-server
lightdm
lightdm-gtk-greeter
feh
picom   桌面透明代理

xorg-xrdb  建议安装，否则.Xresources 的设置无效
xorg-xev 事件提示


code  visual code studio

stlink
openocd

fceux             任天堂模拟器
mame              街机模拟器
desmume           Nintendo DS emulator
snes9x-gtk        Super Nintendo
snes9x            使用提示：not joystick found时，运行加参数 -paddev1 /dev/input/js0
zsnes             Super Nintendo
vbam-sdl          Game Boy Advance
ppsspp            PSP

qgo               围棋
linuxconsole      手柄測試
  jstest /dev/input/js0
moc               mp3 player at console
alsa-utils        音频控制
   arecord -d 10 sample.wav 记录10秒的音频到文件sample.wav中
   aplay sample.wav
lame              mp3 convert
  lame -b 192 --add-id3v2 --id3v2-utf16 --ignore-tag-errors --tt "伦巴达" --ta "n/a" --tl 欧美金唱片 --tn 1/15  audio_01.wav audio_01.mp3
vorbis-tools      ogg encoder
   oggenc -q 3 -o file.ogg file.wav
   oggenc -a artist -t title -l album -G genre -c comment -o file.ogg file.wav
qbittorrent-nox   用浏览器作为UI
e2fsprogs         e2label ext4分区标签

gnuplot                  画二维 
                  plot [x=1:4] 0.5*x*x-3.1

volumeicon        tint2的音量控制
xpdf              pdf reader
cdrtools          ripping sound track抓CD音轨
dosfstools        dos file system utilities

resilio-sync      必须自行下载。运行依赖 libxcrypt-compat
