import json,os,sys,urllib.request as q
U=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("no env")
def po(p,b):
 try:
  with q.urlopen(q.Request(U+p,data=json.dumps(b).encode()))as x:return json.load(x)
 except Exception as e:sys.exit(p)
V=(0,100,320,330,500,900,0)
S=("PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP","!(22(<PU2UZ_2P_d2U_d2PZ_(<PP!(22","<FFFFUPPFZZZFPZZFUUZFPUZFPPP<FFF","PPPUKPPPKPPPKPPPKPPPKPPPUZZZPPPP","<FFKFPUPFUUUPPUUKPUUFPUUFPPP<FFK","dnZPddPPF<<<<22(2((!2((!2((!2((!")
ND=(-33,-31,-18,-14,14,18,31,33);KD=(-17,-16,-15,-1,1,15,16,17);BD=(-17,-15,15,17);RD=(-16,-1,1,16)
M=100000
b=bytearray(128);G=[0,0,-1,0,0];N=[0];L=99999;Z=[0,0];K=[0]*99
class TO(Exception):pass
def pa(f):
 p=f.split();r=7;fl=0
 for i in range(128):b[i]=0
 for ch in p[0]:
  if ch=="/":r-=1;fl=0
  elif ch.isdigit():fl+=int(ch)
  else:
   v="PNBRQKpnbrqk".index(ch)+1;b[r*16+fl]=v;fl+=1
   if v in(6,12):G[2+v//6]=r*16+fl-1
 G[0]=0 if p[1]=="w" else 1
def at(s,w):
 for d,t in zip(((-15,-17)if w==0 else(15,17))+ND+KD,(1,)*2+(2,)*8+(6,)*8):
  q=s+d
  if not q&136 and b[q]==(t if w==0 else t+6):return 1
 for d in KD:
  q=s+d
  while not q&136:
   p=b[q]
   if p:
    if(p>6)==w and(p-1)%6+1 in((3,5)if abs(d)in(15,17)else(4,5)):return 1
    break
   q+=d
 return 0
def gn():
 ms=[];w=G[0]
 for s in range(128):
  if s&136:continue
  p=b[s]
  if not p or(p>6)!=w:continue
  t=p%6 or 6
  if t==1:
   d=16 if w==0 else-16;pr=7 if w==0 else 0;st=1 if w==0 else 6;T=[]
   t1=s+d
   if not b[t1]:
    T.append(t1)
    if(s>>4)==st and not b[s+2*d]:ms.append(s|((s+2*d)<<7))
   for df in(-1,1):
    t1=s+d+df
    if t1&136:continue
    v=b[t1]
    if v and(v>6)!=w:T.append(t1)
   for t1 in T:
    if(t1>>4)==pr:ms.append(s|(t1<<7)|(5<<14))
    else:ms.append(s|(t1<<7))
  else:
   ds=(ND,BD,RD,KD,KD)[t-2];sl=2<t<6
   for d in ds:
    t1=s+d
    while not t1&136:
     v=b[t1]
     if not v:ms.append(s|(t1<<7))
     else:
      if(v>6)!=w:ms.append(s|(t1<<7))
      break
     if not sl:break
     t1+=d
 return ms
def mk(m):
 f=m&127;t=m>>7&127;p=m>>14;pc=b[f]
 b[t]=pc;b[f]=0
 if p:b[t]=p if G[0]==0 else p+6
 if pc==6:G[3]=t
 elif pc==12:G[4]=t
 G[0]^=1
def ev():
 s=0
 for i,p in enumerate(b):
  if i&136 or not p:continue
  t=p%6 or 6;f=i&7;r=i>>4
  v=V[t]+ord(S[t-1][(r if p<7 else 7-r)*4+min(f,7-f)])-80
  s+=v if p<7 else-v
 return s if G[0]==0 else-s
def ic():return at(G[3+(G[0]==1)],G[0]^1)
def od(ms,ply):
 ms.sort(key=lambda m:(50000 if m==K[ply]else 0)+(100000+V[(b[(m>>7)&127]%6 or 6)]*10-V[(b[m&127]%6 or 6)]if b[(m>>7)&127]else 0)+(V[m>>14]*10 if m>>14 else 0),reverse=True)
def qs(a,be,ply):
 N[0]+=1
 if N[0]>L:raise TO
 if ic():
  ms=gn()
  if not ms:return-M+ply
 else:
  s=ev()
  if s>=be:return be
  if s>a:a=s
  ms=[m for m in gn()if b[(m>>7)&127]or m>>14]
 od(ms,ply)
 for m in ms:
  ob=bytes(b);oG=G[:];mk(m)
  if at(G[3+(G[0]==0)],G[0]):b[:]=ob;G[:]=oG;continue
  s=-qs(-be,-a,ply+1)
  b[:]=ob;G[:]=oG
  if s>=be:return be
  if s>a:a=s
 return a
def se(d,a,be,ply):
 N[0]+=1
 if N[0]>L:raise TO
 if d<=0:return qs(a,be,ply)
 ms=gn()
 if not ms:return-M+ply if ic()else 0
 od(ms,ply);best=-M
 for m in ms:
  ob=bytes(b);oG=G[:];mk(m)
  if at(G[3+(G[0]==0)],G[0]):b[:]=ob;G[:]=oG;continue
  s=-se(d-1,-be,-a,ply+1)
  b[:]=ob;G[:]=oG
  if s>best:best=s
  if s>a:a=s
  if a>=be:
   if not b[(m>>7)&127]:K[ply]=m
   break
 return best
def uc(m):
 f=m&127;t=m>>7&127;s=chr(97+f%8)+chr(49+f//16)+chr(97+t%8)+chr(49+t//16)
 p=m>>14
 if p:s+="nbrq"[p-2]
 return s
def ch(fen,legal):
 pa(fen);lg=set(legal);N[0]=0;p=Z[1]
 ms=[m for m in gn()if uc(m)in lg]
 if len(ms)==1:return uc(ms[0])
 Z[0]=ms[0]
 for d in range(1,40):
  try:
   a=-M;be=M
   od(ms,0);bm=ms[0]
   for m in ms:
    ob=bytes(b);oG=G[:];mk(m)
    if at(G[3+(G[0]==0)],G[0]):b[:]=ob;G[:]=oG;continue
    s=-se(d-1,-be,-a,1)
    b[:]=ob;G[:]=oG
    if m==((p>>7&127)|((p&127)<<7)):s-=500
    if s>a:a=s;bm=m
    if a>=be:break
   Z[0]=bm
  except TO:break
 Z[1]=Z[0]
 return uc(Z[0])
while 1:
 g=po("/game",{})
 if g["status"]<"o":break
 while g["status"]>"t":g=po("/move",{"game":g["game"],"move":ch(g["fen"],g["legal_moves"])})
