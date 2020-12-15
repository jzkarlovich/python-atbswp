import time, sys
indent = 0 # how many spaces to indent
indent_increasing = True # Whether the indentation is creasing or not. 

try:
    while True: # The main program loop. 
        print(' ' * indent, end ='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second. 

        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction. 
                indent_increasing = False
            
        else: 
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
