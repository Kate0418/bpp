def ifs(aa,bb):
    O=[ str(i) for i in range(10)]
    if bb=="*" or bb==" " or bb=='{' or bb=='}' or bb=='"':
        return ""
    elif aa=="*" and bb in O:
        return "http://127.0.0.1:1000/gazou/a"+str(bb)+".gif"
    elif bb=="/":
        return "http://127.0.0.1:1000/gazou/sura.gif"
    elif bb==":":
        return "http://127.0.0.1:1000/gazou/tenn.gif"
    else:
        return "http://127.0.0.1:1000/gazou/"+str(bb)+".gif"




def qa(aa, bb, cc, dd):  # 10進数をn進数に変換
    hennkann = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o',
                25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
    
    ws = []
    while True:
        ed = hennkann[int(cc) % bb]
        cc = int(cc) // bb
        ws.append(ed)
        if cc == 0:
            break
    
    ws.reverse()  # 逆順にする
    r = ''.join(ws)
    return r
def rf(aa,bb,cc,dd):#n進数を10進数に変換
    hennkann={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
    t=0
    for j in range(dd):
        for f,g in hennkann.items():
            if g==cc[j]:
                t+=f*(aa**(dd-j-1))
    return t