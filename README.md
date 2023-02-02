# Pwn-Template  
Pwn Solve Template    
使用方法：　　
１.　把模板和其他常用文件放到/home/yurika/pwnlibc/basetools/ 文件夹（根据实际修改），例如：  
 ![image](https://github.com/raddyfiy/cod/blob/master/2020-03-28_153315.png)

2. sudo vim ~/.bashrc
　添加下面的代码到文件里：
 alias gys='FILE=$(ls);chmod 777 ./*;checksec ./*;cp /home/yurika/pwnlibc/basetools/* ./;sed -i s/yyyyyyyyyyyy/$FILE/g pwnsol.py;mv pwnsol.py pwnsol_$FILE.py;subl pwnsol_$FILE.py;'
 
这一句的效果是，如果我们在目标程序的目录里输入gys，会执行以下操作：
赋予程序777权限；执行checksec；把basetools的文件都复制过来；把解题模板里的程序名体替换成真实的程序名；用sublime打开exp文件；
可以根据实际需要修改

3. 生效： 
source ~/.bashrc  

4. 使用：
新建一个空目录，把想要pwn的文件放进去：
https://uploader.shimo.im/f/hpDMwC9e2vyhuavt.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NzUzMDg5MTcsImZpbGVHVUlEIjoiTDlrQk1SbEpkZHM5Tm1xSyIsImlhdCI6MTY3NTMwODYxNywiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjoyNjQyODQzNX0._goYpX2mLpgJbfqdGI_mrurPoinBRuQsorYyB50LRpM![image](https://user-images.githubusercontent.com/23721787/216224808-35c5b027-15fb-4b63-b5d5-7de0d0e2c1ff.png)

执行GYS：

https://uploader.shimo.im/f/iwaeGijZCzjKUNoR.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NzUzMDg5MTcsImZpbGVHVUlEIjoiTDlrQk1SbEpkZHM5Tm1xSyIsImlhdCI6MTY3NTMwODYxNywiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjoyNjQyODQzNX0._goYpX2mLpgJbfqdGI_mrurPoinBRuQsorYyB50LRpM![image](https://user-images.githubusercontent.com/23721787/216224835-07133a20-8050-4419-8c5c-a307fc1da1fb.png)






