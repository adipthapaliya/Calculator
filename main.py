
from tkinter import *
from PIL import Image, ImageTk


root=Tk()
root.title("Calculator")
root.iconbitmap('cal.ico')
root.configure(bg='#000000')

#=====================================================function

def click(number):
    value=e.get()
    e.delete(0,END)
    e.insert(0,str(value)+str(number))

def change_number():
    value=int(e.get())
    e.delete(0,END)
    new_value=value*(-1)
    e.insert(0,new_value)

def clear():
    e.delete(0,END)


def add():
    global f_num
    global math
    math="addition"
    f_num=int(e.get())
    e.delete(0,END)
       

def subtract():
    global f_num
    global math
    math="subtraction"
    f_num=int(e.get())
    e.delete(0,END)

def multi():
    global f_num
    global math
    math="multiplication"
    f_num=int(e.get())
    e.delete(0,END)

def div():
    global f_num
    global math
    math="division"
    f_num=int(e.get())
    e.delete(0,END)

def modulo():
    global f_num
    global math
    math="mod"
    f_num=int(e.get())
    e.delete(0,END)

def equal():
    second_num=int(e.get())
    e.delete(0,END)
    if math=="addition":
        answer=f_num+second_num
        e.insert(0,answer)
    if math=="subtraction":
        answer=f_num-second_num
        e.insert(0,answer)
    if math=="multiplication":
        answer=f_num*second_num
        e.insert(0,answer)
    if math=="division":
        answer=f_num/second_num
        e.insert(0,answer)
    if math=="mod":
        answer=f_num%second_num
        e.insert(0,answer)



#==================================================All image

one = Image.open( "one.jpg")
two = Image.open("two.jpg")
three = Image.open("three.jpg")
four = Image.open("four.jpg")
five = Image.open("five.jpg")
six = Image.open("six.jpg")
seven = Image.open("seven.jpg")
eight = Image.open("eight.jpg")
nine = Image.open("nine.jpg")
zero = Image.open("zero.jpg")
AC = Image.open("ac.jpg")
point = Image.open("point.jpg")
plus = Image.open("plus.jpg")
minus = Image.open("minus.jpg")
product = Image.open("multi.jpg")
divide = Image.open("divide.jpg")
modulus = Image.open("mod.jpg")
change = Image.open("signChange.jpg")
equalto = Image.open("equal.jpg")

#==================================================resize

one_image= one.resize((70,70),Image.ANTIALIAS)
two_image= two.resize((70,70),Image.ANTIALIAS)
three_image= three.resize((70,70),Image.ANTIALIAS)
four_image= four.resize((70,70),Image.ANTIALIAS)
five_image= five.resize((70,70),Image.ANTIALIAS)
six_image= six.resize((70,70),Image.ANTIALIAS)
seven_image= seven.resize((70,70),Image.ANTIALIAS)
eight_image= eight.resize((70,70),Image.ANTIALIAS)
nine_image= nine.resize((70,70),Image.ANTIALIAS)
zero_image= zero.resize((145,70),Image.ANTIALIAS)
AC_image= AC.resize((70,70),Image.ANTIALIAS)
point_image= point.resize((70,70),Image.ANTIALIAS)
plus_image= plus.resize((70,70),Image.ANTIALIAS)
minus_image= minus.resize((70,70),Image.ANTIALIAS)
product_image= product.resize((70,70),Image.ANTIALIAS)
equal_image= equalto.resize((70,70),Image.ANTIALIAS)
divide_image= divide.resize((70,70),Image.ANTIALIAS)
mod_image= modulus.resize((70,70),Image.ANTIALIAS)
change_image= change.resize((70,70),Image.ANTIALIAS)

#====================================================Final image

new_one= ImageTk.PhotoImage(one_image)
new_two= ImageTk.PhotoImage(two_image)
new_three= ImageTk.PhotoImage(three_image)
new_four= ImageTk.PhotoImage(four_image)
new_five= ImageTk.PhotoImage(five_image)
new_six= ImageTk.PhotoImage(six_image)
new_seven= ImageTk.PhotoImage(seven_image)
new_eight= ImageTk.PhotoImage(eight_image)
new_nine= ImageTk.PhotoImage(nine_image)
new_zero= ImageTk.PhotoImage(zero_image)
new_AC= ImageTk.PhotoImage(AC_image)
new_equal= ImageTk.PhotoImage(equal_image)
new_plus= ImageTk.PhotoImage(plus_image)
new_minus= ImageTk.PhotoImage(minus_image)
new_product= ImageTk.PhotoImage(product_image)
new_dvide= ImageTk.PhotoImage(divide_image)
new_mod= ImageTk.PhotoImage(mod_image)
new_point= ImageTk.PhotoImage(point_image)
new_change= ImageTk.PhotoImage(change_image)



#================================================Screen
e=Entry(root,width=20,font=("Helvetica",20),justify="right",bg='black',borderwidth=0,fg="white")
e.grid(row=0,column=0,columnspan=5,ipady=30)

#=============================================Buttons numbers

button_1=Button(root, image=new_one,borderwidth=0,bg="black",command=lambda : click(1))
button_2=Button(root, image=new_two,borderwidth=0,bg="black",command=lambda : click(2))
button_3=Button(root,image=new_three,borderwidth=0 ,bg="black",command=lambda : click(3))
button_4=Button(root, image=new_four,borderwidth=0 ,bg="black",command=lambda : click(4))
button_5=Button(root, image=new_five,borderwidth=0,bg="black",command=lambda : click(5))
button_6=Button(root, image=new_six,borderwidth=0,bg="black",command=lambda : click(6))
button_7=Button(root, image=new_seven,borderwidth=0,bg="black",command=lambda : click(7))
button_8=Button(root, image=new_eight,borderwidth=0,bg="black",command=lambda : click(8))
button_9=Button(root, image=new_nine,borderwidth=0,bg="black",command=lambda : click(9))
button_0=Button(root, image=new_zero,borderwidth=0,bg="black",command=lambda : click(0))

button_point=Button(root, image=new_point,borderwidth=0,bg="black",command=lambda : click("."))

button_add=Button(root, image=new_plus,borderwidth=0,bg="black",command=add)
button_sub=Button(root, image=new_minus,borderwidth=0,bg="black",command=subtract)
button_multi=Button(root, image=new_product,borderwidth=0,bg="black",command=multi)
button_divide=Button(root, image=new_dvide,borderwidth=0,bg="black",command=div)
button_modulo=Button(root, image=new_mod,borderwidth=0,bg="black",command=modulo)
button_signChange=Button(root, image=new_change,borderwidth=0,bg="black",command=change_number)

button_AC=Button(root, image=new_AC,borderwidth=0,bg="black",command=clear)
button_equal=Button(root, image=new_equal,borderwidth=0,bg="black",command=equal)


#================================================Button labeling
button_AC.grid(row=3,column=0)
button_signChange.grid(row=3,column=1)
button_modulo.grid(row=3,column=2)
button_divide.grid(row=3,column=3)

button_7.grid(row=4 ,column=0)
button_8.grid(row=4 ,column=1)
button_9.grid(row=4 ,column=2)
button_add.grid(row=4 ,column=3)

button_4.grid(row=5 ,column=0)
button_5.grid(row=5 ,column=1)
button_6.grid(row=5 ,column=2)
button_sub.grid(row=5 ,column=3)

button_1.grid(row=6 ,column=0)
button_2.grid(row=6 ,column=1)
button_3.grid(row=6 ,column=2)
button_multi.grid(row=6 ,column=3)

button_0.grid(row=7 ,column=0,columnspan=2)
button_point.grid(row=7,column=2)
button_equal.grid(row=7,column=3)





root.mainloop()

