#
#
def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)
#
# 
def swap_case(s):
    st = ""
    st1 = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(s)): 
        st = str(s[i])
        if st in lowercase: st = st.upper()
        else: st = st.lower() 
        st1 = st1 + st           
    return st1