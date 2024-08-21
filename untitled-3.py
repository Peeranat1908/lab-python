#input -> parameter , argument
     #มีหรือไม่มีก็ได้
     #มีกี่ตัวก็ได้
     #ห้ามใช้ global variable เด็ดขาด
#process -> funtion block
#output -> return statement
    #มีหรือไม่มีก็ได้
    #ถ้ามี มีได้แค่ตัวเดียว
    #ถ้่าอยากออกหลายคำ ใช้ tuple , list , dict
    
    
    # pre-defind function
    #เปลี่ยนตัวเลขเป็น'ABC....'
    # 1 -> 'A'
    # 2 -> 'AB'
    # 3 -> 'ABC'
    
def translate(number):
     result = ''
     i = 0
     while i < number:
          result += chr(ord('A') + i)
          i += 1
     return result
     


def main():
     n = int(input("Enter a number: "))
     if n <= 0 or n > 26:
          print("Invalid input, program terminates.")
     else:
          i = 1
          while i <= n : 
               line = translate(i)
               print(line)
               i += 1
          i = n - 1
          while i >= 1:
               line = translate(i)
               print(line)
               i -= 1
main()
#input -> input()
#