import io
import pack
import waybar_socket

'''
unpack返回到参数3是数据到类型/命令
0 退出
1 数值
2 字符串
3 获取值
4 返回值并且增加1
'''
def action(sf):
    data=dict()
    out=io.BytesIO()
    while True:
        conn,addr = sf.accept()
        ok=0
        res=0
        try:
            buf=conn.recv(1000)
            ty,key,val=pack.unpack(buf)
            out.seek(0,io.SEEK_SET)
            if ty==pack.TYPE_INT or ty==pack.TYPE_STR:
                data[key]=val
                pack.resultInt(out,0)
            if ty==pack.TYPE_SHUTDOWN:
                pack.resultInt(out,0)
            if ty==pack.TYPE_GETVALUE:
                if key in data:
                    val=data[key]
                    if isinstance(val,int):
                        pack.resultInt(out,val)
                    if isinstance(val,str):
                        pack.resultStr(out,0,val)
                else:
                    pack.resultStr(out,1,f'"{key}"的内容没有找到')
            if ty==pack.TYPE_VALUE_BEFORE_DEC:
                if key in data:
                    val=data[key]
                    if isinstance(val,int):
                        pack.resultInt(out,val)
                        if val==0:
                            data[key]=0xffff
                        else:
                            data[key]=val-1
                    else:
                        pack.resultStr(out,1,f'"{key}"的内容不是数值')
                else:
                    pack.resultStr(out,1,f'"{key}"的内容没有找到')

            out.truncate()
            conn.sendall(out.getvalue())
            if ty==pack.TYPE_SHUTDOWN:
                break;
        except Exception as e:
            print(e)
        finally:
            conn.close()
def main():
    waybar_socket.skserver(action)
if __name__=="__main__":
    main()
