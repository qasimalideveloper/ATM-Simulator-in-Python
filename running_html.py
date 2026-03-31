import webbrowser

def open_html_file_in_browser(file_path):
    # Open the HTML file in the default web browser
    webbrowser.open(file_path)

if __name__ == "__main__":
    file_path = "project.html"  # Replace with the actual path to your HTML file
    open_html_file_in_browser(file_path)
