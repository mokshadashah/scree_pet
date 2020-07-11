# code for screen pet application 
#!usr/bin/python

from tkinter import *

root = Tk()
# creating a canvas
c = Canvas(root, width=300, height=400)

# configuring its background
c.configure(bg='light sky blue', highlightthickness=0)
c.body_color = 'White'

#making the pet
left_ear = c.create_oval(40,71,120,153, fill = "black", outline = "black")
right_ear = c.create_oval(166,71,246,153, fill = "black", outline = "black")

body = c.create_polygon(92,259,114,234,207,212,196,263,173,307,148,312,123,308, fill = c.body_color, outline = "black", width = 2)

left_hand = c.create_polygon(59,254,84,224,114,235,85,266,77,268,66,268,60,264,59,258,59,252, fill = "black", outline = "black")
right_hand = c.create_polygon(176,233,203,222,224,245,228,253,228,260,222,265,214,268,206,265,198,261,179,240,177,233, fill = "black", outline = "black", state = NORMAL)

face = c.create_oval(40,88,244,242, fill = c.body_color, outline = "black", width = 2)

right_hand_up = c.create_polygon(190,228,218,217,233,199,254,195,257,214,244,234,201,259,200,244,192,229, fill = "black", outline = "black", smooth = 1, state = HIDDEN)

tongue = c.create_oval(137,203,148,217, fill = "salmon", outline = "salmon", state = HIDDEN)
tongue_cover = c.create_oval(139,200,149,207, fill = c.body_color, outline = c.body_color)

left_eye = c.create_polygon(67,166,68,157,82,139,103,130,111,128,118,131,124,139,125,157,120,177,111,192,104,196,101,197,89,196, fill = "black", outline = "black", smooth = 1)
left_circle = c.create_oval(89,135,121,176, fill = c.body_color, outline = "black", state = NORMAL)
left_pupil = c.create_oval(91,140,119,170, fill = "black", outline = "black", state = NORMAL)
left_iris = c.create_oval(105,147,114,157, fill = c.body_color, outline = "black", state = NORMAL)
left_spark = c.create_oval(104,155,109,159, fill = c.body_color, outline = "black",state = NORMAL)

right_eye = c.create_polygon(217,166,216,157,202,139,172,130,160,138,158,159,166,183,172,192,184,198,196,197,216,168, fill = "black", outline = "black", smooth = 1)
right_circle = c.create_oval(162,135,195,176, fill = c.body_color, outline = "black", state = NORMAL)
right_pupil = c.create_oval(164,140,193,170, fill = "black", outline = "black",state = NORMAL)
right_iris = c.create_oval(170,147,179,157, fill = c.body_color, outline = "black",state = NORMAL)
right_spark = c.create_oval(174,155,178,159, fill = c.body_color, outline = "black",state = NORMAL)

nose = c.create_oval(129,181,156,198, fill = "black", outline = "black")
nose_light = c.create_oval(141,183,153,190, fill = c.body_color, outline = "black")
nose_line = c.create_line(143,195,143,207, fill = "black", width = 2)

left_leg = c.create_oval(64,260,128,325, fill = "black", outline = "black")
right_leg = c.create_oval(163,260,227,325, fill = "black", outline = "black")

right_paw = c.create_oval(173,277,219,321, fill = c.body_color, outline = "black")
left_paw = c.create_oval(74,277,120,321, fill = c.body_color, outline = "black")

left_cheek = c.create_oval(75,200,96,217, fill = "pink", outline = "pink", state = HIDDEN)
right_cheek = c.create_oval(187,200,208,217, fill = "pink", outline = "pink", state = HIDDEN)

happy_face = c.create_line(124,200,131,208,143,206,155,208,162,200, fill = "black", smooth = 1, width = 2, state = NORMAL)
sad_face = c.create_line(124,216,131,208,143,206,155,208,162,216, fill = "black", smooth = 1, width = 2, state = HIDDEN)


# making a function to make the eyes blink
def toggle_eyes():
	current_state = c.itemcget(left_circle, 'state')
	new_state = HIDDEN if current_state == NORMAL else NORMAL
	c.itemconfigure(left_circle, state=new_state)
	c.itemconfigure(right_circle,state=new_state)
	c.itemconfigure(left_pupil, state = new_state)
	c.itemconfigure(right_pupil, state = new_state)
	c.itemconfigure(left_iris, state = new_state)
	c.itemconfigure(right_iris, state = new_state)
	c.itemconfigure(left_spark, state = new_state)
	c.itemconfigure(right_spark, state = new_state)
	
	
# calling the function to blink the eyes in another function
def blink():
	toggle_eyes()
	root.after(250, toggle_eyes)
	root.after(1000, blink) 
	
	
# creating a function which will work on event which will 
#make the pet blush if the mouse scrolls within the canvas
def show_happy(event):
	if (20 <= event.x <= 400) and (20 <= event.y <= 500):
		c.itemconfigure(left_cheek, state=NORMAL)
		c.itemconfigure(right_cheek, state=NORMAL)
		c.itemconfigure(happy_face, state = NORMAL)
		c.itemconfigure(sad_face, state = HIDDEN)
		
		
# creating a function which will work on event
# if the mouse isnt on the canvas, it'll be sad
def hide_happy(event):
	c.itemconfigure(left_cheek, state=HIDDEN)
	c.itemconfigure(right_cheek, state=HIDDEN)
	c.itemconfigure(happy_face, state = HIDDEN)
	c.itemconfigure(tongue, state = HIDDEN)
	c.itemconfigure(sad_face, state = NORMAL)


# making function to show the tongue
def toggle_tongue():
	c.itemconfigure(happy_face, state = NORMAL)
	c.itemconfigure(sad_face, state = HIDDEN)
	current_state = c.itemcget(tongue, 'state')
	new_state = NORMAL if current_state == HIDDEN else HIDDEN
	c.itemconfigure(tongue, state = new_state)
	
	
# creating a function which will work on event, 
#if double clicked, it'll show tongue
def show_tongue(event):
		toggle_tongue()
		root.after(1000, toggle_tongue)
		c.itemconfigure(right_hand, state = NORMAL)


# making function to show the the right hand wave
def toggle_hand():
	current_state = c.itemcget(right_hand_up, 'state')
	if current_state == HIDDEN:
			new_state = NORMAL 
			c.itemconfigure(right_hand_up, state = new_state)
			c.itemconfigure(right_hand, state = HIDDEN)
	else:
		c.itemconfigure(right_hand_up, state = HIDDEN)
		c.itemconfigure(right_hand, state = NORMAL)
	

# creating a function which will make the hand wave on an event
def hand_wave(event):
	toggle_hand()
	root.after(1000, toggle_hand)


# creating a button on the canvas
buttonBG = c.create_rectangle(210, 23, 289, 61, fill="lavender", outline="grey60")

# adding text inside the button
buttonTXT = c.create_text(249,40, text="click me!!")

#adding function (left click) on the button to make the hand wave
c.tag_bind(buttonBG, "<Button-1>", hand_wave)

# adding function (left click) on the text to make the hand wave 
c.tag_bind(buttonTXT, "<Button-1>", hand_wave) 

# adding text on canvas
tongueTXT = c.create_text(135,370, text="Double click to get some tonguee :P")

# continous blinking of the pet
root.after(20, blink)

# binding a motion which will show happy if there is motion on the canvas
c.bind('<Motion>', show_happy)

# if the mouse if left the canvas, it'll show sad face
c.bind('<Leave>', hide_happy)

# if double clicked, it'll show its tongue
c.bind('<Double-1>',show_tongue)

c.pack()
root.mainloop()