import PySimpleGUIQt as sg  # Use PySide2 backend

# Set the theme to "Dark Blue 3"
sg.theme("Dark")

# Create the main application window layout
layout = [
    [sg.Button("Button 1"), sg.Button("Button 2")],
    [sg.Button("Settings")]  # Add a button to open the settings menu
]

window = sg.Window("PyCopyBoard", layout, finalize=True)

# Create the settings window layout
settings_layout = [
    [sg.Text("Number of Buttons"), sg.InputText(key="-NUM_BUTTONS-")],
    [sg.Checkbox("Dark Theme", key="-DARK_THEME-")],
    [sg.Button("Save"), sg.Button("Cancel")]
]

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Settings":
        # Open the settings window when the "Settings" button is clicked
        settings_window = sg.Window("Settings", settings_layout, finalize=True)

# Close both windows when done
window.close()
