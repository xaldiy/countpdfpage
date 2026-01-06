#!/usr/bin/env python3
import os as _o,re as _r,base64 as _b
from datetime import datetime as _d
from PyPDF2 import PdfReader as _P

_D=lambda x:_b.b64decode(x).decode(errors="ignore").strip()

def _c(t,f=None,b=None,s=None):
    C={"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenta":35,"cyan":36,"white":37}
    S={"bold":1,"dim":2,"underline":4}
    R="\033[0m";q=""
    if s in S:q+=f"\033[{S[s]}m"
    if f in C:q+=f"\033[{C[f]}m"
    if b in C:q+=f"\033[{C[b]+10}m"
    return f"{q}{t}{R}"

def _bnr():
    for x in (
        "PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0=",
        "8J+ThCBISVRVTkcgSlVNTEFIIEhBTEFNQU4gUERGIE9UT01BVElTIPCfk4Q=",
        "PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0="
    ):print(_c(_D(x),"yellow",s="bold"))
    print(_c(_D("RGlidWF0IG9sZWg6IEFsZGkgU2V0aWFkaSBQdXRyYQ=="),"cyan"))
    print(_c(_D("LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ==\n"),"yellow"))

def _wrn():
    for x in (
        "4pWU4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWX",
        "4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWR",
        "4pWRICAg4pqg77iPICBNT0RFIFRBTlBBIEZJTFRFUiBESU5PTkFLVElGS0FOIOKaoO+4jyAgICAgICAgICAgICDilZE=",
        "4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWR",
        "4pWRICAgR3VuYWthbiBQREYgQ291bnRlciBFeHRyYSAgICAgICAgICAgICAgICAgICAgICAgICAg4pWR",
        "4pWRICAgdW50dWsgc2NhbiBUQU5QQSBmaWx0ZXIgdGFuZ2dhbC4gICAgICAgICAgICAgICAgICAg4pWR",
        "4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWR",
        "4pWRICAgU2NyaXB0IGluaSBXQUpJQiBtZW5nZ3VuYWthbiBmaWx0ZXIgdGFuZ2dhbC4gICAgICAg4pWR",
        "4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWR",
        "4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd"
    ):print(_c(_D(x),"red",s="bold"))

def _num(f):
    n=f.lower()
    if _r.search(r"[a-f0-9]{8}-[a-f0-9]{4}",n):return
    for m in _r.findall(r"\b\d{1,6}\b",n):
        v=int(m)
        if 1<=v<=300000:return v

def _cl(L,g=200):
    L=sorted(set(L))
    if not L:return []
    R=[[L[0]]]
    for x in L[1:]:
        (R[-1] if x-R[-1][-1]<=g else R.append([x])) and R[-1].append(x)
    return R

def _main(L):
    C=_cl(L)
    if not C:return []
    k=max(C,key=len)
    return k if len(k)>=3 else []

def _miss(c,g=200):
    r=[]
    for a,b in zip(c,c[1:]):
        if 1<b-a<=g:r.extend(range(a+1,b))
    return r

def _inp():
    for x in (
        "4pWU4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWX",
        "4pWRIE1hc3Vra2FuIGxva2FzaSBGT0xERVIgUk9PVCB5YW5nIGJlcmlzaSBQREYgICDilZE=",
        "4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd"
    ):print(_c(_D(x),"cyan"))
    return input(_c("   ➡️  ","green",s="bold")).strip('"').strip("'")

def _pd(s):
    for f in ("%d-%m-%Y","%d %B %Y","%d/%m/%Y"):
        try:return _d.strptime(s,f).date()
        except:pass
    raise ValueError

def _dt():
    while True:
        print(_c(_D("UElMSUggRklMVEVSIFRBTkdHQUwgKFdBSklCKTo="),"cyan",s="bold"))
        print(_c(_D("MS4gSGFueWEgZmlsZSBIQVJJIElOSQ=="),"green"))
        print(_c(_D("Mi4gRmlsdGVyIHRhbmdnYWwgdGVydGVudHU="),"yellow"))
        c=input(_c("   ➡️  ","green",s="bold")).strip()
        if c=="1":return _d.now().date()
        if c=="2":
            try:return _pd(input(_c(_D("TWFzdWtrYW4gdGFuZ2dhbCAoREQtTU0tWVlZWSk6IA=="),"cyan")))
            except:print(_c(_D("4p2MIEZvcm1hdCB0YW5nZ2FsIHNhbGFoLg=="),"red"))
        _wrn()

def _scan(r):
    return sorted({p for p,_,f in _o.walk(r) if any(x.lower().endswith(".pdf") for x in f)})

def _proc(d,t):
    N=[]
    print(_c(f"\n📁 {_D('Rm9sZGVyOiA=')}{_o.path.basename(d)}","blue",s="bold"))
    print(_c("────────────────────────────────────────","blue"))
    for f in _o.listdir(d):
        if not f.lower().endswith(".pdf"):continue
        p=_o.path.join(d,f)
        if _d.fromtimestamp(_o.path.getmtime(p)).date()!=t:continue
        try:
            pg=len(_P(p).pages)
            print(_c(f"- {f} ({pg} {_D('bGVtYmFy')})","white"))
        except:
            print(_c(f"- {f} ({_D('KOKdjCBnYWdhbCBiYWNhKQ==')})","red"))
        k=_num(f)
        if k:N.append(k)
    c=_main(N)
    return _miss(c) if c else []

if __name__=="__main__":
    _bnr()
    while True:
        r=_inp()
        if _o.path.isdir(r):break
        print(_c(_D("4p2MIEZvbGRlciB0aWRhayB2YWxpZC4="),"red"))
    d=_dt()
    for x in _scan(r):
        m=_proc(x,d)
        if m:
            print(_c(_D("8J+TiyBGaWxlIGhpbGFuZzo="),"yellow"))
            for z in m:print(_c(f"- {z}.pdf","yellow"))
