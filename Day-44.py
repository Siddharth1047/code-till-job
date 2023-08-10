# Find if the input is a valid IP address or not

def ip_length(n):
    if n >= 0 and n <= 255:
        return True
    return False

def leading_zero(n):
    if len(n) > 1:
        if n[0] == "0":
            return True
    return False

def isValid(s):
    s = s.split(".")

    if len(s) != 4:
        return False
    
    for n in s:
        if leading_zero(n):
            return False
        
        if len(n) == 0:
            return False
        
        try:
            n = int(n)
            if not ip_length(n):
                return False
        except:
            return False
    return True

ip1 = "222.111.111.111"
ip2 = "5555..555"
ip3 = "0000.0000.0000.0000"
ip4 = "1.1.1.1"
print(isValid(ip1))
print(isValid(ip2))
print(isValid(ip3))
print(isValid(ip4))