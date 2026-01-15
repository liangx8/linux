def fill(obj,ft,st,color):
    if ft :
        obj["full_text"]=ft
    if st:
        obj["short_text"]=st
    if color:
        obj["color"]=color
    else:
        obj["color"]="#000000"
#    obj['background']='#aeaeae'
#    obj['border_top']=5
#    obj['border_bottom']=5

Mega = 1024
Giga = Mega * 1024

def sizeStr(s):
    if s> Giga:
        uom='G'
        ss=int(s/Giga)
    elif s > Mega:
        uom='M'
        ss=int(s/Mega)
    else:
        uom='K'
        ss=s
    return "{}{}".format(ss,uom)
