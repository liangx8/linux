import cpu
import time
if __name__ == "__main__":
    cpu.stat()
    c=cpu.Cpu()
    
    time.sleep(1)
    c.update()
    print(c)
