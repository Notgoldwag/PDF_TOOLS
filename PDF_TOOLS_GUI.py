import PySimpleGUI as sg

def main_menu():
    main_label = sg.Text("PDF TOOLS", font=("Helvetica", 20, 'bold'), justification='center')
    split_pdf_button = sg.Button('Split PDF')
    merge_pdf_button = sg.Button('Merge PDF')
    extract_text_button = sg.Button('Extract Text')
    text_to_speech_button = sg.Button('Text to Speech')
    protect_pdf_button = sg.Button('Protect PDF')
    compress_pdf_button = sg.Button('Compress PDF')
    convert_to_png_button = sg.Button('Convert to PNG')
    convert_to_docx_button = sg.Button('Convert to DOCX')
    summarize_text_button = sg.Button('Summarize Text')
    spacer = sg.Text("")
    exit_button = sg.Button('Exit')

    layout = [
        [main_label],
        [split_pdf_button, merge_pdf_button],
        [text_to_speech_button, extract_text_button],
        [protect_pdf_button, compress_pdf_button],
        [convert_to_png_button,convert_to_docx_button],
        [summarize_text_button],
        [spacer],
        [exit_button]
    ]

    window = sg.Window('PDF Tools', layout, size=(400, 350), font=("Times New Roman", 15))

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        else:
            open_tool_window(event)

    window.close()

def open_tool_window(tool_name):
    window = None  # Initialize window variable

    if tool_name == 'Merge PDF':
        merge_pdf_menu_label = sg.Text('Merge PDF Tool',font=("Helvetica", 20, 'bold'), justification='center')

        merge_pdf_input_text = sg.Text("Please select the first PDF    ")
        merge_pdf_input = sg.Input()
        merge_pdf_select_button = sg.FilesBrowse('Choose')

        merge_pdf_spacer = sg.Text("")

        merge_pdf_input_text2 = sg.Text("Please select the second PDF")
        merge_pdf_input2 = sg.Input()
        merge_pdf_select_button2 = sg.FilesBrowse("Choose")

        merge_pdf_input_text3 = sg.Text("Please choose Destination Folder")
        merge_pdf_input3 = sg.Input()
        merge_pdf_select_button3 = sg.FolderBrowse("Choose")


        split_button = sg.Button("Split")

        merge_pdf_layout = [
            [merge_pdf_menu_label],
            [merge_pdf_spacer],
            [merge_pdf_input_text, merge_pdf_input, merge_pdf_select_button],
            [merge_pdf_input_text2, merge_pdf_input2, merge_pdf_select_button2],
            [merge_pdf_input_text3, merge_pdf_input3, merge_pdf_select_button3],
            [split_button]
        ]
        window = sg.Window(tool_name, merge_pdf_layout, size=(850, 350), font=("Times New Roman", 15))
    elif tool_name == 'Split PDF':
        split_pdf_layout = [
            [sg.Text('Merge PDF Tool')],
            [sg.Button('Select PDFs')],
            # Add other elements for specifying merge options
        ]
        window = sg.Window(tool_name, split_pdf_layout)
    # Add elif blocks for other tool layouts
    
    while True:
        if window:  # Check if window is initialized
            event, _ = window.read()

            if event == sg.WIN_CLOSED:
                break

    if window:  # Close window if it's open
        window.close()
if __name__ == "__main__":
    main_menu()
