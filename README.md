# Pwn-Template    [RGB-TEAM出品]
Pwn Solve Template   v1.0   
##功能介绍：
自动填写程序名与识别系统libc；   
自动获取onegadget列表；  
自动获取程序架构；  
堆题栈题通用；  
支持程序爆破；  
远端和本地方便切换，libc方便切换，把精力集中在程序本身；  
调试器支持，使用ida()即可等待ida链接，建议配合https://github.com/anic/ida2pwntools使用 
添加各种助记信息



## 一、使用方法-建议环境准备：　　
### 1.　把模板和其他常用文件放到/home/yurika/pwnlibc/basetools/ 文件夹（根据实际修改），例如：  
 ![image](https://github.com/raddyfiy/cod/blob/master/2023-02-02_111230.png)

### 2. sudo vim ~/.bashrc   

添加下面的代码到文件里   


alias gys='FILE=$(ls);chmod 777 ./*;checksec ./*;cp /home/yurika/pwnlibc/basetools/* ./;sed -i s/yyyyyyyyyyyy/$FILE/g pwnsol.py;mv pwnsol.py pwnsol_$FILE.py;subl pwnsol_$FILE.py;'   
 
这一句的效果是，如果我们在目标程序的目录里输入gys，会执行以下操作：  

赋予程序777权限；执行checksec；把basetools的文件都复制过来；把解题模板里的程序名体替换成真实的程序名；用sublime打开exp文件；
可以根据实际需要修改  

### 3. 生效： 
source ~/.bashrc   

### 4. 使用：  

新建一个空目录，把想要pwn的文件放进去：  
 ![image](https://github.com/raddyfiy/cod/blob/master/2023-02-02_113014.png)

执行GYS：
 ![image](https://github.com/raddyfiy/cod/blob/master/2023-02-02_113059.png)

## 二、使用方法-模板的使用



# RGB的其他项目：
https://github.com/RGBTeam/ctf-RGB-wiki



