'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
P_file = os.path.join(directory, 'test_image.jpg')

# Open and show the student image in a new Figure window
P_img = PIL.Image.open(P_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(P_img, interpolation='none')

P_file = os.path.join(directory, 'test_image.jpg')
P_img = PIL.Image.open(P_file)
P_large = P_img.resize((650, 400)) #eye width and height measured in plt
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(P_img)
axes3[1].imshow(P_large)
fig3.show()

# Display student in second axes and set window to the right eye
axes[1].imshow(P_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 1000))
axes[1].set_xlim(410, 530) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(175, 20)
fig.show()

# Open, resize, and display earth
Ep_file = os.path.join(directory, 'crest.png')
Ep_img = PIL.Image.open(Ep_file)
 #eye width and height measured in plt
 
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(Ep_img)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
P_large.paste(Ep_img, (0, 200), mask=Ep_img) 
# Display
fig4, axes4 = plt.subplots(1, 2)
axes4[0].imshow(P_large, interpolation='none')
axes4[1].imshow(P_large, interpolation='none')
axes4[1].set_xlim(650, 0)
axes4[1].set_ylim(410,0)
fig4.show()