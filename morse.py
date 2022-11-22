#importing the required modules
from tkinter import *
from tkinter import messagebox

root = Tk()

variable1 = StringVar(root)
variable2 = StringVar(root)

variable1.set("SELECT")
variable2.set("SELECT")

#Creating a dictionary to map characters with morse codes
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#creating a function to clear all the texts in both the text fields
def clearAll(lang1, lang2):
    lang1.delete(1.0, END)
    lang2.delete(1.0, END)

#creating a function to detect the language and initialize converting
def convert(lang1, lang2):

    #changing all the text in the text field to run the program correctly
    message = lang1.get("1.0", "end")[:-1].upper()

    #showing an error message if the user gave both language as same 
    if variable1.get() == variable2.get():
        messagebox.showerror("Can't be same language")
        return

    #encryprting the message if English ot morse
    elif variable1.get() == "English" and variable2.get() == "Morse":
        result = encrypt(message)
    
    #decrypting the message if Morse to english
    elif variable1.get() == "Morse" and variable2.get() == "English":
        result = decrypt(message)
    
    else :
        messagebox.showerror("Please choose valid language ")
        return
    
    #inserting the result into the second textfield
    lang2.insert("end -1 chars", result)

#creating a function to encrypt the given message
def encrypt(message):

    #setting a cipher variable to store the encrypted message
    cipher = ''

    for letter in message:
     
        #adding the encryption with a space at the end to recognize easily
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '

        else :
            cipher += ' '
    
    #returning the cipher 
    return cipher 

#creating a function to decrypt the given message
def decrypt(message):
    
    #adding a space at the end to access the last morse code
    message += ' '

    #setting a decipher variable to store the decrypted message
    decipher = ''
    text = ''

    for letter in message :
        if letter != ' ':
            i = 0
            text += letter 
        else :
            i += 1
            if i == 2:
                decipher += ' '
            else :
                #accessing the keys using their values
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(text)]
                text = ''
    
    #returning the decipher
    return decipher

#creating a function to display how to use 
def help():
    master = Tk()

    #configuring the help window to black color
    master.configure(bg = "black")

    #setting geometry for the help window
    master.geometry("660x180")
    
    Label(master, text = "How To Use", bg = "black", fg = "blue", font = "TimesNewRoman 20").pack()

    instructions = """Select the language modes using the option menu for both fields
    Type the message to be translated in the first text field
    Click on the CONVERT button to show the result
    If you want to clear the texts click on the CLEAR button"""

    insLabel = Label(master, text = instructions, bg = "black", fg = "white", font = "TimesNewRoman 16",padx = 5, pady = 2)
    insLabel.pack()
    master.mainloop()
#creating main function
def main():

    #configuring the background color of the window
    root.configure(bg = "black")

    #setting the geometry
    root.geometry("600x530")
    
    #setting the title
    root.title("Morse Translator")

    #creating a label for heading
    head = Label(root, text = "Morse CODE Translator", fg = "green", bg = "black", font = ("TimesNewRoman", 20))
    head.pack()

    #creating a button for how to use
    helpButton = Button(root, text = "Help", bg = "black", fg = "white", font = "TimesNewRoman 8", padx = 3, command = help)
    helpButton.place(x = 5, y = 3)

    #list of languages for option menu
    languageCodeList = ["English", "Morse"]

    fromSelectionLabel = Label(root, text = "Select Language Mode", fg = "white", bg = "black", font = ("TimesNewRoman",12))
    fromSelectionLabel.place(x = 10, y = 50)

    #creating a option menu for first language
    fromLangOption = OptionMenu(root, variable1, *languageCodeList)
    fromLangOption.configure(bg = "black", fg = "white", padx = 20)
    fromLangOption.place(x = 200, y = 50)

    #creating a text field for first language
    language1_field = Text(root, height = 7, width = 64, font = "lucida 13")
    language1_field.place(x = 10, y = 90)

    
    toSelectionLabel = Label(root, text = "Select Laguage Mode", fg = "white", bg = "black", font = "TimesNewRoman 12")
    toSelectionLabel.place(x = 10, y = 240)

    #creating a option menu for second language
    toLangOption = OptionMenu(root, variable2, *languageCodeList)
    toLangOption.configure(bg = "black", fg = "white", padx = 20)
    toLangOption.place(x = 200, y = 240)

    #creating a textField for second language
    language2_field = Text(root, height = 7, width = 64, font = "lucida 13")
    language2_field.place(x = 10, y = 280)

    #creating a button to clear all the text in both textFields
    clearButton = Button(root, text = "CLEAR", bg = "black", fg = "red", font = "TimesNewRoman 12", padx = 110, pady = 15, command = lambda: clearAll(language1_field, language2_field))
    clearButton.place(x = 10, y = 450)

    #creating the button for executing the convert function
    convertButton = Button(root, text = "CONVERT", bg = "black", fg = "blue", font = "TimesNewRoman 12", padx = 100, pady = 15, command = lambda: convert(language1_field, language2_field))
    convertButton.place(x = 300, y = 450)

    #mainlooping the tk window
    root.mainloop()


if __name__ == '__main__':
    main()
    


    

