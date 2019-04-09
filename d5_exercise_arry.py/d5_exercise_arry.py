#定义原始数组
arr=[0,1,2,3,4,5,6,7,8,9]
#将数组[0,1,2,3,4,5,6,7,8,9,]翻转
arr.reverse()
#print('this is a reserved aray:',arr )
#将翻转后的数组拼接成字符串
str1=''.join(str(i) for i in arr)
#用字符串切片的方式取出第三到第八个字符（包括第三个和第八个字符）
str2=str1[3:9]
#将获得的字符串进行翻转
str3=str2[::-1]
#将获得的结果转换为int类型
int1=int(str3)
#分别转换为二进制，八进制，十六进制
#最后输出三种进制的结果
print('十进制整数为：',int1)
print('转换成二进制为：',bin(int1))
print('转换成八进制为:',oct(int1))
print('转换成十六进制为:',hex(int1))