#home work
#i/p aaabbbccc
#o/p a=2b=3
st=input()
finish=''
f=[]
for ch in st:
    if ch not in finish:
        print(ch,st.count(ch))
        finish+=ch
