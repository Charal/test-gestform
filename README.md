# test-gestform

Install dependencies : pip install numpy

Launch unit test :
python tests/test_methods_unittest.py


Generate list of 10 integer number, between range of -1000 and 1000, for each number in the list, we want to do the following:

• if the number is divisible by 3: out is "Geste"

• if the number is divisible by 5: out is "Forme"

• if the number is divisible by 3 and by 5: out is "Gestform"

• otherwise: out is the number

Command line :
python divided_by.py    

Out example :

    -250 >> Forme
    
    -920 >> Forme
    
    608 >> 608
    
    -344 >> -344
    
    -788 >> -788
    
    -693 >> Geste
    
    840 >> Gestform
    
    363 >> Geste
    
    -684 >> Geste
    
    -713 >> -713
    


