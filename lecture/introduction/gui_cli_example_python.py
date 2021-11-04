import os
from pathlib import Path
import shutil

for name in ['pugsley', 'gomez', 'foster']:
    
    if not os.path.exists('/Users/peerherholz/Desktop/adams_family/%s' %name):
        os.makedirs('/Users/peerherholz/Desktop/adams_family/%s' %name)
    
    os.chdir('/Users/peerherholz/Desktop/adams_family/%s' %name)
   
    for id in range(1,11):

        Path('scooby_do_%s.txt' %str(id)).touch()

    if not os.path.exists('/Users/peerherholz/Desktop/the_new_yorker'): 
        os.makedirs('/Users/peerherholz/Desktop/the_new_yorker')

    for file in os.listdir("./"):

        if int(file.rsplit(".txt", 1)[0].rsplit('_', 1)[1])%2==0:
            shutil.move(file, '/Users/peerherholz/Desktop/the_new_yorker/%s' %file.replace('.txt', '_%s.txt' %name))