'''
This file handles all the UI and interaction with the user
'''
import dearpygui.dearpygui as dpg #Main library
from PIL import Image #image loading
import time #For animations

#Load image using PIL and convert to DearPyGui
def load_image(file_path):
    image = Image.open(file_path)
    width, height = image.size
    image_data = image.tobytes()
    return width, height, image_data

# Callback function to show the intro mode page 
def intro_callback(sender, app_data):
    dpg.hide_item("main")
    show_page("intro_pg")

#Callback function to show the playlist mode page 
def play_callback(sender, app_data):
    dpg.hide_item("main")
    show_page("search_pg")

def show_page(page_tag):
    if(page_tag == "intro_pg"):
        dpg.show_item("intro_pg")

    
# Create the GUI
dpg.create_context()

#Font Registration
with dpg.font_registry():
    regular_font = dpg.add_font("/mnt/c/users/andyh/Documents/Card-Access-Playlist-Project/fonts/Figtree-Regular.ttf", 72)
    header_font = dpg.add_font("/mnt/c/users/andyh/Documents/Card-Access-Playlist-Project/fonts/Figtree-Bold.ttf", 80)
#Loading image
width, height, image_data = load_image("/mnt/c/users/andyh/Documents/Card-Access-Playlist-Project/qr.png")

#Texture Register
with dpg.texture_registry():
     dpg.add_static_texture(width, height, image_data, tag="qr")

#Main Window
with dpg.window(tag = "Primary_Window", width=800, height=600):
    dpg.bind_font(regular_font) #Bind default font
    ##Main Page
    with dpg.group(tag= "main", horizontal=False): #Header
        dpg.add_spacer(height= 10) 
        with dpg.group(horizontal=True):
            dpg.add_spacer(width = 10)
            h1 = dpg.add_text("Please Select a Operation Mode:" ,tag= "header_text")
            dpg.bind_item_font(h1,header_font)
    #Operation Buttons
        dpg.add_spacer(height = 20) 
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=10)
            dpg.add_button(label="Intro", tag = "intro_button", width=338, height=152, callback = intro_callback, )
            dpg.add_spacer(width=100)  
            dpg.add_button(label="Playlist",tag = "playlist_button", width=338, height=152, callback = play_callback, )

    #Exit Button
    dpg.add_button(label="Exit", tag = "exit_button" ,width=338, height=152, callback= lambda: dpg.stop_dearpygui(), pos=(1532,798))
    ##Intro Page
    with dpg.group(tag = "intro_pg", horizontal= False):
        dpg.add_spacer(height = 20)
        with dpg.group(horizontal= True):
            dpg.add_spacer(width = 20)
            dpg.add_image("qr", width = 400, height=400)
            dpg.add_spacer(width = 20)
            dpg.add_text("Register songs at the site above")
        
        with dpg.group(horizontal = True):
            dpg.add_spacer(width = 20)
            dpg.add_text("Register songs at the site above")
            
        dpg.add_text("Waiting...", tag= "wait",pos= (960, 540))
        dpg.bind_item_font("wait",header_font)
    

dpg.hide_item("intro_pg") 

# Set up and run the GUI
dpg.create_viewport(title='Music X Player', width=1280, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary_Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
