lightdm
lightdm-gtk-greeter
openbox
tint2 桌面状态条 https://gitlab.com/o9000/tint2
xorg-xrdb  建议安装，否则.Xresources 的设置无效

code  visual code studio

stlink
openocd

fceux             任天堂模拟器
mame              街机模拟器
desmume           Nintendo DS emulator
snes9x-gtk        Super Nintendo
zsnes             Super Nintendo
vbam-sdl          Game Boy Advance
ppsspp            PSP

qgo               围棋
linuxconsole      手柄測試
  jstest /dev/input/js0
qbittorrent-nox
mocp              mp3 player at console
alsa-utils        音频控制
   arecord -d 10 sample.wav 记录10秒的音频到文件sample.wav中
   aplay sample.wav
lame              mp3 convert
  lame -V 5 -add-id3v2 --pad-id3v2 --ignore-tag-errors -ta artist -tl album -tt title --tn track -ty year -tg genre -tc comment file.wav file.mp3
vorbis-tools      ogg encoder
   oggenc -q 3 -o file.ogg file.wav
   oggenc -a artist -t title -l album -G genre -c comment -o file.ogg file.wav
qbittorrent-nox   用浏览器作为UI
js60              javascript shell, 装visual studio code的依赖
e2fsprogs         e2label ext4分区标签

gnuplot                  画二维 
                  plot [x=1:4] 0.5*x*x-3.1

volumeicon        tint2的音量控制
xpdf              pdf reader
