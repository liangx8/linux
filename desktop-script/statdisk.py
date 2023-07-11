import other

class StatDisk(dict):
    ''' read /proc/diskstats '''
    def __init__(self,disks):
        with open('/proc/diskstats','r') as st:
            self.__d1=stat()
            self.__disks=disks

        
    def update(self):
        other.fill(self,"calcuting ...",None,None)
    def between(self,d2):
        d=self.__d1
        for r in d:
            for r1 in d2:
                if r[2] == r1[2]:
                    for ix in range(3,len(r)):
                        r[ix]=r1[ix]-r[ix]
        self.__d1=d2
        return d
    def show(self):
        d2=stat()
        d=self.between(d2)
        show(d)
        for dks in self.__disks:
            for r in d:
                if r[2]==dks:
                    if r[6]==0:
                        print(dks,"read 0/s")
                    else:
                        print(dks,"read",r[5]/r[6]*1000)
                    if r[10]==0:
                        print(dks,"write 0/s")
                    else:
                        print(dks,"write", r[9]/r[10]*1000)
        
def show(d):
    print("-------------------------------------")
    for x in d:
        print(x)
    
def stat():
    with open('/proc/diskstats','r') as st:
        data=[]
        for li in st:
            row=li.split()
            nrow=[]
            for n in range(len(row)):
                if n==2:
                    nrow.append(row[n])
                else:
                    nrow.append(int(row[n]))
            data.append(nrow)
        return data
'''

Field  1 -- # of reads completed (unsigned long)
    This is the total number of reads completed successfully.

Field  2 -- # of reads merged, field 6 -- # of writes merged (unsigned long)
    Reads and writes which are adjacent to each other may be merged for
    efficiency.  Thus two 4K reads may become one 8K read before it is
    ultimately handed to the disk, and so it will be counted (and queued)
    as only one I/O.  This field lets you know how often this was done.

Field  3 -- # of sectors read (unsigned long)
    This is the total number of sectors read successfully.

Field  4 -- # of milliseconds spent reading (unsigned int)
    This is the total number of milliseconds spent by all reads (as
    measured from blk_mq_alloc_request() to __blk_mq_end_request()).

Field  5 -- # of writes completed (unsigned long)
    This is the total number of writes completed successfully.

Field  6 -- # of writes merged  (unsigned long)
    See the description of field 2.

Field  7 -- # of sectors written (unsigned long)
    This is the total number of sectors written successfully.

Field  8 -- # of milliseconds spent writing (unsigned int)
    This is the total number of milliseconds spent by all writes (as
    measured from blk_mq_alloc_request() to __blk_mq_end_request()).

Field  9 -- # of I/Os currently in progress (unsigned int)
    The only field that should go to zero. Incremented as requests are
    given to appropriate struct request_queue and decremented as they finish.

Field 10 -- # of milliseconds spent doing I/Os (unsigned int)
    This field increases so long as field 9 is nonzero.

    Since 5.0 this field counts jiffies when at least one request was
    started or completed. If request runs more than 2 jiffies then some
    I/O time might be not accounted in case of concurrent requests.

Field 11 -- weighted # of milliseconds spent doing I/Os (unsigned int)
    This field is incremented at each I/O start, I/O completion, I/O
    merge, or read of these stats by the number of I/Os in progress
    (field 9) times the number of milliseconds spent doing I/O since the
    last update of this field.  This can provide an easy measure of both
    I/O completion time and the backlog that may be accumulating.

Field 12 -- # of discards completed (unsigned long)
    This is the total number of discards completed successfully.

Field 13 -- # of discards merged (unsigned long)
    See the description of field 2

Field 14 -- # of sectors discarded (unsigned long)
    This is the total number of sectors discarded successfully.

Field 15 -- # of milliseconds spent discarding (unsigned int)
    This is the total number of milliseconds spent by all discards (as
    measured from blk_mq_alloc_request() to __blk_mq_end_request()).

Field 16 -- # of flush requests completed
    This is the total number of flush requests completed successfully.

    Block layer combines flush requests and executes at most one at a time.
    This counts flush requests executed by disk. Not tracked for partitions.

Field 17 -- # of milliseconds spent flushing
    This is the total number of milliseconds spent by all flush requests.
'''
