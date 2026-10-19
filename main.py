# Participation Activity 2
from pyscript import display, document

grade8 = {'Max Mayfield', 'Dustin Henderson', 'Jane Hopper'} # set 1
grade9 = {'Jonathan Byers', 'Nancy Wheeler', 'Steve Harrington'} # set 2
grade10 = {'Adrianna Allas', 'Katharine Penas', 'Margaretha Magsino'} # set 3
new_members = {'Jaena Ambata', 'Mikela Santiago'} # set 4
total_members = grade8.union(grade9, grade10, new_members) # Union

display(f'All members: {grade8, grade9, grade10, new_members}', target='output') 
display(f'Total members: {len(total_members)}', target='output') # displaying the function