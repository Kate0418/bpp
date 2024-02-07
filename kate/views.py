from django.shortcuts import render,redirect
from .forms import formA,formB,formC
import sympy
from .ifs import ifs,qa,rf
import json
# Create your views here.
def qq(aa):
    return render(aa,"kate/kate.html")
def ww(aa):
    try:
        qq=formA(aa.GET)
        url=[]
        uu=""
        if qq.is_valid():
            qq=qq.cleaned_data['qq']
            one=[ str(i) for i in range(10)]
            A=[ chr(i) for i in range(97, 123)]
            for i in str(qq):
                if i not in one and i not in A and i!="+" and i!="-" and i!="(" and i!=")" and i!="/":
                    raise Exception("Invalid character in input")
            ww=len(qq)
            ee=qq[0]
            rr=0
            tt=0
            yy=0
            tukau=[]
            for i in range(1,ww):
                if qq[i] in one:
                    rr=1
                elif qq[i] in A:
                    rr=2
                if qq[i-1] in one:
                    tt=1
                elif qq[i-1] in A:
                    tt=2
                if qq[i]=="(":
                    if qq[i-1]!="+" and qq[i-1]!="-":
                        ee+="*"
                elif rr==1 :
                    if tt==2 or qq[i-1]==")":
                        ee+="**"
                elif rr==2:
                    if qq[i] not in tukau:
                        tukau.append(qq[i])
                    if tt!=0 or qq[i-1]==")":
                        ee+="*"
                ee+=qq[i]
                rr=0
                tt=0
                yy=0
            sympy.var(tukau)
            kekka=sympy.factor(ee)
            ii=0
            for i in str(kekka):
                if i=="*":
                    ii+=1
                else:
                    if ii==2 and i in one:
                        uu+="*"
                    else:
                        ii=0
                    uu+=i
            url=[ ifs(uu[i-1],uu[i]) for i in range(1,len(uu)) if ifs(uu[i-1],uu[i]) != " "]
        if uu=="":
            uu=["*"]
        context={
            "form":formA,
            "url":url,
            "uu":ifs(0,uu[0]),
        }
        return render(aa,"kate/insuu.html",context)
    except Exception as e:
        return redirect("http://127.0.0.1:8000/era")
def ee(aa):
    try:
        qq=formB().qq(aa.GET)
        ww=formB().ww(aa.GET)
        ee=formB().ee(aa.GET)
        ans=""
        if qq.is_valid() and ww.is_valid() and ee.is_valid():
            a= int(qq.cleaned_data['qq'])
            b= int(ww.cleaned_data['ww'])
            c= ee.cleaned_data['ee']
            one=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for i in str(c):
                if i not in one[:a]:
                    raise Exception("Invalid character in input")
            d=len(str(c))
            if a==b:
                ans=c
            elif a==1:
                ans=int(qa(10,b,len(str(c)),len(str(len(c)))))
            elif b==1:
                ans=str(0)*int(rf(a,10,c,d))
            elif a==10:
                ans=qa(a,b,c,d)
            elif b==10:
                ans=rf(a,b,c,d)
            else:
                ans=qa(10,b,rf(a,10,c,d),len(str(rf(a,10,c,d))))
        
        context={
            "form":formB,
            "ans":ans
        }
        return render(aa,"kate/sinsuu.html",context)
    except Exception as e:
        return redirect("http://127.0.0.1:8000/era")
def rr(aa):
    try:
        qq=formA(aa.GET)
        url=[]
        uu=""
        if qq.is_valid():
            qq=qq.cleaned_data['qq']
            one=[ str(i) for i in range(10)]
            A=[ chr(i) for i in range(97, 123)]
            for i in str(qq):
                if i not in one and i not in A and i!="+" and i!="-" and i!="(" and i!=")" and i!="/":
                    raise Exception("Invalid character in input")
            ww=len(qq)
            ee=qq[0]
            rr=0
            tt=0
            yy=0
            tukau=[]
            for i in range(1,ww):
                if qq[i] in one:
                    rr=1
                elif qq[i] in A:
                    rr=2
                if qq[i-1] in one:
                    tt=1
                elif qq[i-1] in A:
                    tt=2
                if qq[i]=="(":
                    if qq[i-1]!="+" and qq[i-1]!="-":
                        ee+="*"
                elif rr==1 :
                    if tt==2 or qq[i-1]==")":
                        ee+="**"
                elif rr==2:
                    if tt!=0 or qq[i-1]==")":
                        ee+="*"
                ee+=qq[i]
                rr=0
                tt=0
                yy=0
            if "**" in ee:
                raise Exception("Invalid character in input")
            kekka=sympy.solve(ee)
            ii=0
            for i in kekka:
                if i=="*":
                    ii+=1
                else:
                    if ii==2 and str(i) in one:
                        uu+="*"
                    else:
                        ii=0
                    uu+=str(i)
            url=[ ifs(uu[i-1],uu[i]) for i in range(1,len(uu))]
        if uu=="":
            uu=["*"]
        context={
        "form":formA,
        "url":url,
        "uu":ifs(0,uu[0]),
        }
        return render(aa,"kate/houtei1.html",context)
    except Exception as e:
        return redirect("http://127.0.0.1:8000/era")
            
def tt(aa):
    try:
        qq=formA(aa.GET)
        url=[]
        uu=""
        if qq.is_valid():
            qq=qq.cleaned_data['qq']
            one=[ str(i) for i in range(10)]
            A=[ chr(i) for i in range(97, 123)]
            for i in str(qq):
                if i not in one and i not in A and i!="+" and i!="-" and i!="(" and i!=")" and i!="/":
                    raise Exception("Invalid character in input")
            ww=len(qq)
            ee=qq[0]
            rr=0
            tt=0
            yy=0
            tukau=[]
            for i in range(1,ww):
                if qq[i] in one:
                    rr=1
                elif qq[i] in A:
                    rr=2
                if qq[i-1] in one:
                    tt=1
                elif qq[i-1] in A:
                    tt=2
                if qq[i]=="(":
                    if qq[i-1]!="+" and qq[i-1]!="-":
                        ee+="*"
                elif rr==1 :
                    if tt==2 or qq[i-1]==")":
                        ee+="**"
                elif rr==2:
                    if tt!=0 or qq[i-1]==")":
                        ee+="*"
                ee+=qq[i]
                rr=0
                tt=0
                yy=0
            kekka=sympy.solve(ee)
            ii=0
            pp=""
            oo=""
            for i in range(len(kekka)):
                pp+=str(kekka[i])
                if i!=len(kekka)-1:
                    pp+=","
            for i in pp:
                if i=="s":
                    ii+=1
                    oo+=i
                elif i=="q" and ii==1:
                    ii+=1
                    oo+=i
                elif i=="r" and ii==2:
                    ii+=1
                    oo+=i
                elif i=="t" and ii==3:
                    ii+=1
                    oo+=i
                elif oo=="sqrt" and i=="(":
                    uu+="$"
                    uu+="("
                    oo=""
                else:
                    ii=0
                    uu+=oo
                    oo=""
                    uu+=i
            url=[ ifs(uu[i-1],uu[i]) for i in range(1,len(uu))]
        if uu=="":
            uu=["*"]
        context={
        "form":formA,
        "url":url,
        "uu":ifs(0,uu[0]),
        }
        return render(aa,"kate/houtei2.html",context)
    except Exception as e:
        return redirect("http://127.0.0.1:8000/era")
def yy(aa):
    try:
        url=[]
        uu=""
        qq=formC().qq(aa.GET)
        ww=formC().ww(aa.GET)
        if qq.is_valid() and ww.is_valid():
            qq=qq.cleaned_data['qq']
            ww=ww.cleaned_data["ww"]
            one=[ str(i) for i in range(10)]
            A=[ chr(i) for i in range(97, 123)]
            for i in str(qq):
                if i not in one and i not in A and i!="+" and i!="-" and i!="(" and i!=")" and i!="/":
                    raise Exception("Invalid character in input")
            for i in str(ww):
                if i not in one and i not in A and i!="+" and i!="-" and i!="(" and i!=")" and i!="/":
                    raise Exception("Invalid character in input")
            WW=len(qq)
            ee=qq[0]
            rr=0
            tt=0
            yy=0
            tukau=[]
            for i in range(1,WW):
                if qq[i] in one:
                    rr=1
                elif qq[i] in A:
                    rr=2
                if qq[i-1] in one:
                    tt=1
                elif qq[i-1] in A:
                    tt=2
                if qq[i]=="(":
                    if qq[i-1]!="+" and qq[i-1]!="-":
                        ee+="*"
                elif rr==1 :
                    if tt==2 or qq[i-1]==")":
                        ee+="**"
                elif rr==2:
                    if qq[i] not in tukau:
                        tukau.append(qq[i])
                    if tt!=0 or qq[i-1]==")":
                        ee+="*"
                ee+=qq[i]
                rr=0
                tt=0
                yy=0
            if "**" in ee or len(tukau)!=2:
                raise Exception("Invalid character in input")
            sympy.var(tukau)
            kekka1,ee=ee,ww[0]
            WW=len(ww)
            for i in range(1,WW):
                if ww[i] in one:
                    rr=1
                elif ww[i] in A:
                    rr=2
                if ww[i-1] in one:
                    tt=1
                elif ww[i-1] in A:
                    tt=2
                if ww[i]=="(":
                    if ww[i-1]!="+" and ww[i-1]!="-":
                        ee+="*"
                elif rr==1 :
                    if tt==2 or ww[i-1]==")":
                        ee+="**"
                elif rr==2:
                    if ww[i] not in tukau:
                        tukau.append(ww[i])
                    if tt!=0 or ww[i-1]==")":
                        ee+="*"
                ee+=ww[i]
                rr=0
                tt=0
                yy=0
            if "**" in ee or len(tukau)!=2:
                raise Exception("Invalid character in input")
            kekka2=ee
            kekka=sympy.solve([kekka1, kekka2])
            uu=str(kekka)
            url=[ ifs(uu[i-1],uu[i]) for i in range(1,len(uu))]
        if uu=="":
            uu=["*"]

        context={
            "form":formC,
            "url":url,
            "uu":ifs(0,uu[0])
        }
        return render(aa,"kate/renritu.html",context)
    except Exception as e:
        return redirect("http://127.0.0.1:8000/era")
def uu(aa):
    return render(aa,"kate/era.html")