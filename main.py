# Participation Activity 2
from pyscript import display, document

def member_checker(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('first').value
    last_name = document.getElementById('surname').value
    full_name = first_name + ', ' + last_name

    grade7 = {'Holly Wheeler', 'Derek Turnbow', 'Debbie Miller'}
    grade8 = {'Max Mayfield', 'Dustin Henderson', 'Jane Hopper'} 
    grade9 = {'Jonathan Byers', 'Nancy Wheeler', 'Steve Harrington'}
    grade10 = {'Adrianna Allas', 'Katharine Penas', 'Margaretha Magsino'}
    total_members = grade7 | grade8 | grade9 | grade10 # Union
    total_members.add(full_name)

    display(f'All members: {total_members}', target='output') 
    display(f'Total members: {len(total_members)}', target='output') # displaying the function
