import webview


class App:
    def __init__(self):
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
            "HTML Label Example BARFOO", html=html_content, frameless=False
        )

        # Expose the print_hello_world function to JavaScript
        self.webview_window.expose(self.print_hello_world)

        # Close Event
        self.webview_window.events.closed += self.on_exit

    def start(self):
        webview.start(lambda a: None, self.webview_window, gui="tkinter", debug=False)

    def on_exit(self):
        print("Window Destroyed")

    def print_hello_world(self):
        print("Hello World")


# Create the main Tkinter window
app = App()
app.start()
