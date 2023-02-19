def fill(obj,ft,st,color):
    if ft :
        obj["full_text"]=ft
    if st:
        obj["short_text"]=st
    if color:
        obj["color"]=color
    else:
        obj["color"]="#1003ae"
    obj['background']='#aeaeae'
#    obj['border_top']=5
#    obj['border_bottom']=5
