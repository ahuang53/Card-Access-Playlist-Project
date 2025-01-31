'''
This file handles all the UI and interaction with the user
'''
import dearpygui.dearpygui as dpg #Main library
from PIL import Image,ImageFont #image loading
import time #For animations
import threading #Continuously running functions
import main
import os

#Global variable to control the intro mode checking
intro_thread = True
#Global variable to add a song to the local playlist
local_song = ""

#Load image using PIL and convert to DearPyGui
def load_image(file_path):
    image = Image.open(file_path)
    width, height = image.size
    image_data = image.tobytes()
    return width, height, image_data

# Callback function to switch to the intro mode page 
def intro_callback(sender, app_data):
    dpg.hide_item("main")
    dpg.show_item("intro_pg")
    print(main.local_playlist)
    #intro_loop()
'''
#Function to continously check for entries in intro mode 
def intro_loop():
    main.intro_mode()
    global intro_thread
    if not intro_thread:
        intro_thread = True
        thread = threading.Thread(target=intro_check, daemon=True)
        thread.start()
'''
'''
#Function to help check for intro mode entries
def intro_check():
    global intro_thread
    while intro_thread:
        time.sleep(0.5)  # Simulating a periodic task
        main.intro_mode()
'''
    
#Callback function to switch to the search pg of playlist mode page 
def sg_callback(sender, app_data):
    dpg.hide_item("main")
    dpg.hide_item("play_pg")
    dpg.show_item("play_s_pg")

#Callback function to show queue playlist page 
def play_callback(sender,app_data):
    dpg.hide_item("play_s_pg")
    dpg.show_item("play_pg")
    main.playlist_mode()

#Callback function to switch hide all other pages other than home 
def return_to_home(sender, app_data):
    #Stop any threads:
    global intro_thread
    intro_thread = False

    dpg.show_item("main")
    dpg.hide_item("play_pg")
    dpg.hide_item("intro_pg")
    dpg.hide_item("play_s_pg")
    
#Callback function to search the scanner result
def scan_search(sender, app_data):
    code = dpg.get_value(sender)
    main.intro_mode(code)
    
#Callback function to generate a confirmation window
def show_info(selection_callback, prompt_font):
    message = "Is this correct: \n" #If statement to become an erorr statement if needed
    title = "Confirmation" #If statement to be Error
    search_name = dpg.get_value("search_bar_1")
    search_auth = dpg.get_value("search_bar_2")
    response = main.searching(search_name,search_auth)
    if(response[0] == 0):
        title = "ERROR"
        message = response[1]
    else:
        message += response[1].full_title
        global local_song 
        local_song = response[1]
    # guarantee these commands happen in the same frame
    with dpg.mutex():

        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()

        with dpg.window(label = title, modal=True, no_close=True, width=580, height=270) as modal_id:
            m1 = dpg.add_text(message)
            dpg.bind_item_font(m1 , prompt_font)
            if(response[0] != 0):
                with dpg.group(horizontal = True):
                    b_yes = dpg.add_button(label="Yes", width=75, user_data=(modal_id, True), callback=selection_callback)
                    dpg.bind_item_font(b_yes , prompt_font)
                    dpg.add_spacer(width = 20)
                    b_no = dpg.add_button(label="No", width=75, user_data=(modal_id, False), callback=selection_callback)
                    dpg.bind_item_font(b_no , prompt_font)
            else:
                with dpg.group(horizontal = True):
                    b_yes = dpg.add_button(label="Close", user_data=(modal_id, True), callback=selection_callback)
                    dpg.bind_item_font(b_yes , prompt_font)

    # guarantee these commands happen in another frame
    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2 , viewport_height // 2 - height // 2])

#Callback confirming the song
def on_selection(sender, app_data, user_data):
    if user_data[1]:
        print("User selected 'Yes'")
        main.local_playlist.append(local_song)
    else:
        print("User selected 'No'")
    # delete window
    dpg.delete_item(user_data[0])

#Callback to shuffle the playlist
def shuffle(sender, app_data):
    print("shuffled")
    main.playlist_control("shuffle")

#Callback to resume the playlist
def pause_play(sender, app_data):
    print("resumed")
    if(dpg.get_value("status") == "Stopped..."):
        dpg.set_value("status", "Playing...")
    else:
        dpg.set_value("status", "Stopped...")
    main.playlist_control("play")

'''
###############################################################################
def center_space():
    window_width = dpg.get_item_width("Primary_Window")
    print("WIndow: {}".format(window_width))
    text_width = 345 # Get the width of the text
    print("textwdith: {}".format(text_width))
    spacer_width = (window_width - text_width) / 2  # Calculate the width of spacers on each side
    print("Spacer: {}".format(spacer_width))

def get_text_size(text, font_path, font_size):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the size of the text
    bbox = font.getbbox(text)

    width = bbox[2] - bbox[0]  # x_max - x_min
    height = bbox[3] - bbox[1]  # y_max - y_min
    
    return width, height  # returns (width, height)

 #Spacing checker
        #width, height = get_text_size("Waiting...", "/mnt/c/users/andyh/Documents/Card-Access-Playlist-Project/fonts/Figtree-Bold.ttf", 80)
        #print(f"Text size: Width = {width}, Height = {height}")
        #dpg.add_button(label = "koads", callback= lambda:center_space() )
#################################################################################
    '''
def setup_ui():
    # Create the GUI
    dpg.create_context()

    #Font Registration
    with dpg.font_registry():
        regular_font = dpg.add_font(r"C:\Users\AndyH\Shared with ND\Latest Card Access Files\Card-Access-Playlist-Project\fonts\Figtree-Regular.ttf", 60)
        prompt_font =  dpg.add_font(r"C:\Users\AndyH\Shared with ND\Latest Card Access Files\Card-Access-Playlist-Project\fonts\Figtree-Regular.ttf", 40)
        bigger_font = dpg.add_font(r"C:\Users\AndyH\Shared with ND\Latest Card Access Files\Card-Access-Playlist-Project\fonts\Figtree-Regular.ttf", 72)
        header_font = dpg.add_font(r"C:\Users\AndyH\Shared with ND\Latest Card Access Files\Card-Access-Playlist-Project\fonts\Figtree-Bold.ttf", 80)
            
    #Loading image
    width, height, image_data = load_image(r"C:\Users\AndyH\Shared with ND\Latest Card Access Files\Card-Access-Playlist-Project\qr.png")

    #Texture Register
    with dpg.texture_registry():
        dpg.add_static_texture(width, height, image_data, tag="qr")

    #Main Window
    with dpg.window(tag = "Primary_Window", width=800, height=600): #800, 600
        dpg.bind_font(regular_font) #Bind default font

        ##Main Page
        with dpg.group(tag= "main", horizontal=False): #Header
            dpg.add_spacer(height= 30) 
            with dpg.group(horizontal=True):
                dpg.add_spacer(width = 440) 
                dpg.add_text("Please Select a Operation Mode:" ,tag= "header_text")
                dpg.bind_item_font("header_text",header_font)
        
        #Operation Buttons
            dpg.add_spacer(height = 260) 
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=259)
                dpg.add_button(label="Intro", tag = "intro_button", width=400, height=180, callback = intro_callback, )
                dpg.bind_item_font("intro_button",bigger_font)
                dpg.add_spacer(width=518)  
                dpg.add_button(label="Playlist",tag = "playlist_button", width=400, height=180, callback = sg_callback, )
                dpg.bind_item_font("playlist_button",bigger_font)
        ##Intro Page
        with dpg.group(tag = "intro_pg", horizontal= False):
            #Songpicker website
            dpg.add_spacer(height = 20)
            with dpg.group(horizontal= True):
                dpg.add_spacer(width = 20)
                dpg.add_image("qr", width = 400, height=400)
                dpg.add_spacer(width = 20)
                dpg.add_text("Register songs at the site to the left", tag = "info_text")
                dpg.bind_item_font("info_text",bigger_font)
    
            #Intro Mode Status
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 802)
                dpg.add_text("Waiting...", tag= "wait")
                dpg.bind_item_font("wait",header_font)
            dpg.add_spacer(height = 10)
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 620)
                dpg.add_input_text(tag = "intro_scan",width = 600, hint= "Click here and scan",
                                   on_enter=True, callback = scan_search)
        ##Search Page
        with dpg.group(tag = "play_s_pg", horizontal = False):
            dpg.add_spacer(height = 20)
            #Switch to control the playlist playback
            dpg.add_button(label="Queue", tag = "queue_button" ,width=280, height=128, callback= play_callback, pos=(1610,30))
            dpg.bind_item_font("queue_button",bigger_font)

            #Search Bars and Text
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 20)
                dpg.add_text("Enter Song Title", tag= "title")
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 20)
                dpg.add_input_text(tag="search_bar_1",  hint="Type to search...")
            dpg.add_spacer(height = 20)
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 20)
                dpg.add_text("Enter Artist Name", tag= "author")
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 20)
                dpg.add_input_text(tag="search_bar_2",  hint="Type to search...")  
            dpg.add_spacer(height = 20)  
            with dpg.group(horizontal = True): 
                dpg.add_spacer(width = 20)
                dpg.add_button(label = "Search for song", tag = "search_button", 
                            callback=lambda:show_info(on_selection,prompt_font))
        
        #Exit Button
        dpg.add_button(label="Exit", tag = "exit_button" ,width=280, height=128, callback= lambda: dpg.stop_dearpygui(), pos=(1610,850))
        dpg.bind_item_font("exit_button",bigger_font)
        #Home Button
        dpg.add_button(label="Home", tag = "home_button" ,width=280, height=128, callback= return_to_home, pos=(1310,850))
        dpg.bind_item_font("home_button",bigger_font)

        ##Playlist Page
        with dpg.group(tag = "play_pg", horizontal = False):
            dpg.add_button(label="Return", tag = "return_button" ,width=280, height=128, callback= sg_callback, pos=(1010,850))
            dpg.bind_item_font("return_button",bigger_font)
            dpg.add_text("Current Playlist: \n", tag = "current_play")
            #Status and control of playlist
            dpg.add_spacer(height = 200)
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 790)
                dpg.add_text("Status:") #Add playing / stopped logic
                dpg.add_text(" Stopped...",  tag = "status")
            dpg.add_spacer(height = 20)
            with dpg.group(horizontal = True):
                dpg.add_spacer(width = 500)
                dpg.add_button(label="Shuffle", tag = "shuffle_button", width=280, height=128, callback = shuffle, )
                dpg.bind_item_font("shuffle_button",bigger_font)
                dpg.add_spacer(width = 20)
                dpg.add_button(label="Play", tag = "playback_button", width=280, height=128, callback = pause_play, )
                dpg.bind_item_font("playback_button",bigger_font)
                dpg.add_spacer(width = 20)
                dpg.add_button(label="Pause", tag = "stop_play_button", width=280, height=128, callback = pause_play, )
                dpg.bind_item_font("stop_play_button",bigger_font)
            #add temporary message below shuffle 

    return_to_home(None,None) #Hides all other pages 
    # Set up GUI
    dpg.create_viewport(title='Music X Player', width=1280, height=720)
    #All other setups
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary_Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    setup_ui()
