def correct(fxn = 'default' ):
    if fxn == 'default':
        print('\n              please rerun the program\n')
    else:
        print('''
              please enter the correct value
              ''')
        fxn()
correct()