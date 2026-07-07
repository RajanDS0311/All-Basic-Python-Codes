F1 = open("India.txt","w")
F1.write("India is an Asian Country.\nIts capital is New Delhi.")
F1.close()

F1 = open("India.txt","r")
print(F1.read())
F1.close()