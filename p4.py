#######################################################################
# Computer Project #4
# 
# Algorithm
#
#   Main function is called. After initializing variables Main calls the 
#   the function get_ch. This function will test for appropraite entry
#   (single character) and return that character. Main will then call get state
#   to determine the "state" the character entry is in. This process will 
#   continue to loop until user inputs Return/Enter. The output to the user
#   is dependent on the final state of the entry before pressing enter. This
#   output is then printed.
#
########################################################################


def get_ch():
    
    """
    By using a while loop / try and except user input is validated via the
    parameters specified. The input character is only returned if it is a 
    single character. If not a value error is raised and message is displayed.
    
    """
    # prompt for the input in a loop
    

    while True:
        
        ch = input("Enter a character or press the Return key to finish: ")   

        try:
            
            # if entry is more than a single character ask again for input
        
            if len(ch) == 1 or ch == "":
    
                # return the character
                
                return ch
            
            else:
            
                raise ValueError
    
           #  in case of invalid input, print the following error message
           
        except ValueError:
                
            print("Invalid input, please try again.")
            
            # return the ch at the end

def find_state(state, ch):
    
    """
    This function receives two parameters - the current state when the function
    is called and the next character to be evaluated. Through use of an if/elif
    tree the function returns the proper state based on the beginning state and
    the character.
    
    """
    
    # evaluates characters in state 1
    
    if state == 1:
        
        if ch == "h":
            
            state = 2
            
            return state
        
        else:
            
            state = 5
            
            return state
        
    # evaluates characters in state 2
            
    elif state == 2:
        
        if ch == "a" or ch == "o":
            
            state = 3
            
            return state
        
        else:
            
            state = 5
            
            return state
        
    # evaluates characters in state 3    
        
    elif state == 3:
        
        if ch == "!":
            
            state = 4 
            
            return state
        
        elif ch == "h":
            
            state = 2
            
            return state
        
        else:
            
            state = 5
            
            return state
        
    # evaluates characters in state 4

    elif state == 4:
        
        state = 5
        
        return state
    
    # evaluate characters in state 5
    
    elif state == 5:
        
        return state

def main():
    
    """
    This function drives the program. It begins by displaying introduction 
    information then initializes variables. Next, it enters a while loop until
    the entry is empty. While inside the while loop get_ch() is called and the
    state of that character is determined, then appending the character to a
    string. This process is continued until Enter/Return is entered, exiting 
    the loop and displaying the results.
    
    """

    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    # initialize the variables
    
    string = ""
    
    ch = " "
    
    state = 1
    
    # call the functions in a loop
    
    while ch != "":
        
        ch = get_ch()
        
        if ch == "":
            
            break
        
        else:
        
            string += ch
        
            state = find_state(state,ch)
            

        
        
    # when user enters an empty string print the results
    
    print("\nYou entered", string)
        
    if state == 4:
        
        print("You are laughing.")
        
    elif state != 4:
    
        print("You are not laughing.")

main()