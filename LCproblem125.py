s=s.lower()
        new=""
        
        for char in s:
            if char.isalnum():#in this particular line was using s.islaum which is wrong as i wasnt checking the specific char.
                new+=char
        
        if new==new[::-1]:#new thing learnt if i want to reverse a string in python i  will be using this [::-1]
            return True
        else:
            return False
        #on course of this problem i learned the different syntaxs that are used in python to manipulate strings in python and how to implement them.
