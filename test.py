import dearpygui.dearpygui as dpg

# Callback function for the search button
def search_callback(sender, app_data, user_data):
    search1 = dpg.get_value("search_input1")
    search2 = dpg.get_value("search_input2")
    dpg.set_value("output_text", f"Search 1: {search1}, Search 2: {search2}")

# Create the GUI
dpg.create_context()
with dpg.font_registry():
    proggy_font = dpg.add_font("NotoSerifCJKjp-Medium.otf", 30)  # Larger size of ProggyClean

with dpg.window(tag = "Primary Window", width=800, height=600):
    dpg.add_text("Please select an operational mode:", tag= "header_text")
    dpg.add_text("Enter Search 1:")
    dpg.add_input_text(tag="search_input1")
    
    dpg.add_text("Enter Search 2:")
    dpg.add_input_text(tag="search_input2")
    
    dpg.add_button(label="Search", callback=search_callback)
    dpg.add_button(label="Cancel", callback=lambda: dpg.stop_dearpygui())
    
    dpg.add_text("", tag="output_text")  # To display output below buttons

# Assign the larger font to the header text
dpg.bind_item_font("header_text", proggy_font)

# Set up and run the GUI
dpg.create_viewport(title='Music X Player', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
