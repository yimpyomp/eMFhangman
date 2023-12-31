full_hang = r'''

                           _____________________
                          /                    |
                          |                  ------
                          |                 /      \
                          |                |        |
                          |                 \      /
                          |                  ------
                          |                    |
                          |                    |
                          |                    |
                          |             -------|-------
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                   / \
                          |                  /   \
                          |                 /     \
                          |                /       \
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''


stage_only = r'''
                           _____________________
                          /                    |
                          |                  
                          |                       
                          |                
                          |                 
                          |                  
                          |                    
                          |                    
                          |                    
                          |             
                          |                    
                          |                    
                          |                    
                          |                    
                          |                    
                          |                  
                          |                  
                          |                
                          |                
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''

one_wrong = r'''
                           _____________________
                          /                    |
                          |                  ------
                          |                 /      \
                          |                |        |
                          |                 \      /
                          |                  ------
                          |                    
                          |                    
                          |                    
                          |             
                          |                    
                          |                    
                          |                    
                          |                    
                          |                    
                          |                
                          |                
                          |                
                          |                
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''

two_wrong = r'''
                           _____________________
                          /                    |
                          |                  ------
                          |                 /      \
                          |                |        |
                          |                 \      /
                          |                  ------
                          |                    |
                          |                    |
                          |                    |
                          |                    |             
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                
                          |                
                          |                
                          |                
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''

three_wrong = r'''
                           _____________________
                          /                    |
                          |                  ------
                          |                 /      \
                          |                |        |
                          |                 \      /
                          |                  ------
                          |                    |
                          |                    |
                          |                    |
                          |                    |-------             
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                
                          |                
                          |                
                          |                
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''

four_wrong = r'''
                           _____________________
                          /                    |
                          |                  ------
                          |                 /      \
                          |                |        |
                          |                 \      /
                          |                  ------
                          |                    |
                          |                    |
                          |                    |
                          |             -------|-------            
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                
                          |                
                          |                
                          |                
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''

five_wrong = r'''
                           _____________________
                          /                    |
                          |                  ------
                          |                 /      \
                          |                |        |
                          |                 \      /
                          |                  ------
                          |                    |
                          |                    |
                          |                    |
                          |             -------|-------            
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                    |
                          |                   /
                          |                  /
                          |                 /
                          |                /
                          |
                          |
                          |
                          |
                          |
------------------------------------------------------------------------------
'''


def draw_stage(attempts_remaining):
    if attempts_remaining == 6:
        return stage_only
    if attempts_remaining == 5:
        return one_wrong
    if attempts_remaining == 4:
        return two_wrong
    if attempts_remaining == 3:
        return three_wrong
    if attempts_remaining == 2:
        return four_wrong
    if attempts_remaining == 1:
        return five_wrong
    else:
        return full_hang
