def middle_n(s, n):
    """Returns the middle n characters from a string.
    middle_n("abcdcba", 3) returns "cdc"
    Default toward the end of the list if the selection does not line up exactly.
    middle_n("abcdcba", 4) returns "cdcb"
    This one is more difficult! Use intermediate variables to keep track of values."""
    
    string_length = len(s)
    
    #print(string_length)
     
    midpoint = string_length // 2
    #print("Midpoint is: ",midpoint)
    #print(s[midpoint])

    #find the slice based upon N now
    #subtract 1 from N becuase we already have the midpoint
    #num_steps = n -1


    #n IS ODD
    if n % 2 != 0:

        step_val = n // 2
        slice_point_start = midpoint - step_val
        #we add 1 to the stop point bc pythong string slicing goes up to but does not include the number so you have to go one more to get it
        slice_point_stop = midpoint + step_val + 1
        #print(slice_point_start)
      

        print("The middle: ", n," charachters of string ", s," is",s[slice_point_start:slice_point_stop])
    #n IS EVEN
    else:
        step_val = n // 2

        slice_point_start = midpoint - step_val  
        slice_point_stop = midpoint + step_val
        
        #this was the really hard corner case to lock down. If the lenght of the string is odd and the number you want to pull out is even. 
        #you need to add 1 for the math to work in this edge case.
        if (string_length % 2) !=0:
            slice_point_start += 1
            slice_point_stop += 1
        
        print("The middle: ", n," charachters of string ", s," is",s[slice_point_start:slice_point_stop])

middle_n("abcd",1)
middle_n("abcd",2)
middle_n("abcd",3)
middle_n("abcd",4)
middle_n("abcd",5)

middle_n("abcde",1)
middle_n("abcde",2)
middle_n("abcde",3)
middle_n("abcde",4)
middle_n("abcde",5)
middle_n("abcde",6)


print("---------even strings---------")
middle_n("abcdcb", 3)
middle_n("abcdcb", 4)

print("-----example test strings------")
middle_n("abcdcba",1)
middle_n("abcdcba",2)
middle_n("abcdcba",3)
middle_n("abcdcba",4)
middle_n("abcdcba",5)
middle_n("abcdcba",6)
middle_n("abcdcba",7)



