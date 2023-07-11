import statdisk
import cpu
import time
def sd():
    c=statdisk.StatDisk(("sda","sdb"))
    c.update()
    time.sleep(1)
    c.show()
def core():
    c=cpu.Cpu()
    time.sleep(2)
    c.update()
    print(c)
if __name__ == "__main__":
    core()
    #battery.findBattery()
