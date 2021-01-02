def validIPAddresses(string):
    # Write your code here.
    IPAddresses = []
    
    getIPs(string, IPAddresses, 0, 0)
    
    for ip in IPAddresses:
        print(ip)
    
    return IPAddresses
            
def getIPs(string, IPs, leftIdx, count, current = []):
    if count == 3:
        IP_right = string[leftIdx:]
        if validateIP(IP_right):
            current.append(IP_right)
            IPs.append(''.join(current))
            current.pop()
        return
    
    for i in range(leftIdx, leftIdx+3):
        rightIdx = i+1
        
        if rightIdx > len(string):
            return
        IP_left = string[leftIdx:rightIdx]
        if validateIP(IP_left):
            current.append(IP_left+'.')
            
            getIPs(string, IPs, rightIdx, count+1, current)
    
            if len(current):
                current.pop()
        
def validateIP(string):
    if len(string):
        if string[0] == '0' and len(string) > 1:
            return False
        IP_substr = int(string)
        if IP_substr >= 0 and IP_substr <= 255:
            return True
    return False


IP = '1921680'
IP = '3700100'
print(IP,'\n')
answer = validIPAddresses(IP)
# print(answer)