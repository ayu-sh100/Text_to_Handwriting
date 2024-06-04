import pywhatkit as p
txt = input("Enter the txt: ")
# here in these function the second and te third parameter are optional
# second parameter is the file name where the image will be saved
# and third is the colour by default its blue but we can change it according to our need.
p.text_to_handwriting(txt,"img.png",[0,0,138])