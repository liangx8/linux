import other
ic_play='\uf04b'
ic_forward='\uf04e'
ic_backward='\uf04a'
ic_pause='\uf04c'
ic_mute='\uf026'
ic_unmute='\uf028'

class MpvControl(dict):
    def __init__(self):
        self['background']='#3423da'
        other.fill(self,"{} {} {} {}".format(ic_backward,ic_play,ic_forward,ic_mute),None,'#908010')
    def thread_run(self):
        pass
    def update(self):
        pass
