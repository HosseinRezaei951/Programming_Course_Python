A = eval(input("Please enter the  first number(integer): "))
B = eval(input("Please enter the  second number(integer): "))
C = eval(input("Please enter the  Third number(integer): "))

if ( A <= B and A <= C and B <= C ):
            
            print ( "Sort three integers in increasing order is : \n"
                    , A ,"\n"
                    , B ,"\n"
                    , C )

elif ( not(A <= B) ) :

            t = B
            B = A
            A = t
            if ( A <= C and B <= C ):

                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )

            elif ( (not(A <= C )) and B <= C ) :

                        t = A
                        A = C
                        C = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )

            elif ( A <= C and (not(B <= C)) ) :
                        
                        t = C
                        C = B
                        B = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )


                        
            elif ( (not(A <= C )) and (not(B <= C)) ) :

                        t = A
                        A = C
                        C = t
                        
                        t = C
                        C = B
                        B = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )

elif ( A <= B and (not(A <= C)) ) :

            if ( (not(A <= C )) and B <= C ) :

                        t = A
                        A = C
                        C = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )

            elif ( A <= C and (not(B <= C)) ) :
                        
                        t = C
                        C = B
                        B = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )


                        
            elif ( (not(A <= C )) and (not(B <= C)) ) :

                        t = A
                        A = C
                        C = t
                        
                        t = C
                        C = B
                        B = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )

elif ( A <= B and A <= C and (not(B <= C)) ) :
 
                        t = C
                        C = B
                        B = t
                        print ( "Sort three integers in increasing order is : \n"
                                , A ,"\n"
                                , B ,"\n"
                                , C )

      

            

            
                   
                   

            
            
