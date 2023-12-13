'''fonction check_salute'''
def verifier_salutations(couloir):
    salutations = 0
    for i in range(len(couloir)):
        if couloir[i] == '>' and '<' in couloir[i+1:]:
            salutations += couloir[i+1:].count('<')
        elif couloir[i] == '<' and '>' in couloir[i+1:]:
            salutations += couloir[i+1:].count('>')
    return salutations