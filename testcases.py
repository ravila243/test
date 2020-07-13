""" TEST CASES """
def test_cases():
    total = 0
    if twenty_nineteen() == 2019:
        print('q1t1: Test Passed!')
        total+=1
    else:
        print('q1t1: Test Failed')
        print('Expected: 2019')
        print('Got: ' + str(twenty_nineteen()))

    print('')         
    print(str(total/1 * 100) + '% Correct')

              
test_cases() 
