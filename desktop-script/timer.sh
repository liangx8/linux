#!/bin/sh
# 关于定时器到帮助查看 man systemd.timer(5)
# 缺省单位是秒
# m - 分钟, h - 小时
systemd-run --user --on-active="$1" mpg123 /home/com/mp3/ring/南澤大介\ -\ Victory.mp3
