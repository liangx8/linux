#手动切换桌面背景
import wallpaper
import mylog
import sys
if __name__ == "__main__":
    log=mylog.Log(sys.stdout)
    wallpaper.Wallpaper('/home/com/wallpaper/',log).update()
    log.flush()
    
