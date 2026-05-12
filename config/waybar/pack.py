TYPE_SHUTDOWN         = 0
TYPE_INT              = 1
TYPE_STR              = 2
TYPE_GETVALUE         = 3
TYPE_VALUE_BEFORE_GET = 4

def int2b4(v):
    return v.to_bytes(4,'little')
def b2int(b):
    return int.from_bytes(b,'little')
class Pack():
    def __init__(self,key,value):
        self.__key=key
        self.__value=value
    def value(self):
        return self.__value
    def writekey(self,out):
        out.write(int2b4(self.__key))

class PackInt(Pack):
    def writeTo(self,out):
        out.write(int2b4(TYPE_INT))
        self.writekey(out)
        out.write(int2b4(self.value()))
class PackStr(Pack):
    def writeTo(self,out):
        out.write(int2b4(TYPE_STR))
        self.writekey(out)
        buf=self.value().encode()
        out.write(int2b4(len(buf)))
        out.write(buf)
class PackShutdown(Pack):
    def __init__(self):
        pass
    def writeTo(self,out):
        out.write(int2b4(TYPE_SHUTDOWN))
class PackGetValue(Pack):
    def __init__(self,key):
        super().__init__(key,None)
    def writeTo(self,out):
        out.write(int2b4(TYPE_GETVALUE))
        self.writekey(out)
class PackValueBeforeGet(PackGetValue):
    def writeTo(self,out):
        out.write(int2b4(TYPE_VALUE_BEFORE_GET))
        self.writekey(out)

def resultInt(out,val):
    out.write(int2b4(0)) # allways success
    out.write(int2b4(TYPE_INT))
    out.write(int2b4(val))
def resultStr(out,code,val):
    out.write(int2b4(code))
    buf=val.encode()
    out.write(int2b4(TYPE_STR))
    out.write(int2b4(len(buf)))
    out.write(buf)


def unpack(buf):
    ty=b2int(buf[:4])
    if ty==TYPE_INT:
        key=b2int(buf[4:8])
        return ty,key,b2int(buf[8:12])
    if ty==TYPE_STR:
        key=b2int(buf[4:8])
        size=b2int(buf[8:12])
        return ty,key,buf[12:size+12].decode()
    if ty==TYPE_GETVALUE or ty==TYPE_VALUE_BEFORE_GET:
        key=b2int(buf[4:8])
        return ty,key,None
    return ty,None,None

def unresult(buf):
    code=b2int(buf[:4])
    ty=b2int(buf[4:8])
    if ty==TYPE_INT:
        val=b2int(buf[8:12])
    if ty==TYPE_STR:
        size=b2int(buf[8:12])
        val=buf[12:12+size].decode()
    return code,val
