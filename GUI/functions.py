from password_Generator_GUI import *
from ui import *

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from pyperclip import copy

class UIFunctions(MainWindow):
    
    # set default length to 8
    password_Length = 8
    
    # update the length of password when slider is moved
    def update_Length(self):
        UIFunctions.password_Length = self.UIMainwindow.horizontalSlider_Length.value()
        self.UIMainwindow.lineEdit_Length_Number.setText(str(UIFunctions.password_Length))
        
    # show password in the lineEdit
    def display_Password(self, password):
        self.UIMainwindow.lineEdit_Password.setText(password)
        
    # generate the password
    def generate_Password(self, include_Numbers, include_Symbols, include_Uppercase, include_Lowercase):
        password = ''
        
        for i in range(UIFunctions.password_Length):
            # generate random characters
            random_Number = choice(digits)
            random_Symbol = choice(punctuation)
            random_Uppercase = choice(ascii_uppercase)
            random_Lowercase = choice(ascii_lowercase)  
            
            # check which characters to include
            include = []
            if include_Numbers:
                include.append(random_Number)
            if include_Symbols:
                include.append(random_Symbol)
            if include_Lowercase:
                include.append(random_Lowercase)
            if include_Uppercase:
                include.append(random_Uppercase)
            if include == []:
                include.append(random_Number)
                include.append(random_Uppercase)
                include.append(random_Lowercase)
                include.append(random_Symbol)
        
            # add random character to password
            password += choice(include)
        
        UIFunctions.display_Password(self, password)
        
        # copy password to clipboard
        copy(password)
        
        return password