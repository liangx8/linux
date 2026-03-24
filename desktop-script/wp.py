#手动切换桌面背景
import i3status
import wallpaper
import mylog
import sys
if __name__ == "__main__":
    log=mylog.Log(sys.stdout)
    cfg=i3status.config("i3status.cfg")
    wallpaper.Wallpaper(cfg['wallpaper'],log).update()
    log.flush()
    
