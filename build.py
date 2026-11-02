"""Inject content/deep/*.js into index.html and write the Claude artifact copy."""
import glob,re,sys
p='index.html'; s=open(p,encoding='utf8').read()
deep="const DEEP={};\n"+"\n".join(open(f,encoding='utf8').read() for f in sorted(glob.glob('content/deep/*.js')))
s=re.sub(r'/\*DEEP\*/[\s\S]*?/\*/DEEP\*/',lambda m:'/*DEEP*/'+deep+'/*/DEEP*/',s,count=1)
qx="const QX={};\n"+"\n".join(open(f,encoding='utf8').read() for f in sorted(glob.glob('content/quiz/*.js')))
s=re.sub(r'/\*QX\*/[\s\S]*?/\*/QX\*/',lambda m:'/*QX*/'+qx+'/*/QX*/',s,count=1)
open(p,'w',encoding='utf8').write(s)
head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
a=s[len(head):].replace('</head>\n<body>\n','',1).rstrip()
a=a[:-len('</body>\n</html>')]
open(sys.argv[1] if len(sys.argv)>1 else '/home/claude/noor-elearning.html','w',encoding='utf8').write(a)
print('ok',len(s))
