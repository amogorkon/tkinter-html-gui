import tkinter as tk

import webview


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML GUI Example")

        # Sample HTML content with a custom button
        html_content = """
        <html>
            <body>
                <h1>Welcome to the App</h1>
                <button id="helloButton">Click here to print Hello World</button>
                <script>
                    document.getElementById('helloButton').addEventListener('click', function(event) {
                        event.preventDefault();
                        window.pywebview.api.print_hello_world();
                    });
                </script>
            </body>
        </html>
        """

        # Create a webview window
        self.webview_window = webview.create_window(
            "HTML GUI Example (Webview Window)", html=html_content, frameless=False
        )

        # Expose the print_hello_world function to JavaScript
        self.webview_window.expose(self.print_hello_world)
        self.webview_window.events.closed += self.on_exit

        # Start the webview
        self.start_webview()

    def start_webview(self):
        webview.start(self.on_start, self.webview_window, debug=False)

    def on_start(self, window):
        print("Window started")

    def on_exit(self):
        print("Window closed")
        self.root.destroy()

    def print_hello_world(self):
        print("Hello World")


# Create the main Tkinter window
root = tk.Tk()
app = App(root)
root.withdraw()  # Hide the Tkinter root window
root.protocol("WM_DELETE_WINDOW", app.on_exit)  # Handle window close event
root.mainloop()
