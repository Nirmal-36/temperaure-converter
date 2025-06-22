from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Button, Static
from textual.reactive import reactive

class TemperatureApp(App):
    CSS_PATH = "temp_app.css"
    fahrenheit = reactive("")
    celsius = reactive("")

    def compose(self) -> ComposeResult:
        yield Static("🌡️ Temperature Converter", classes="header")
        yield Input(placeholder="Enter Celsius (e.g., 100)", id="celsius_input")
        yield Button("Convert to Fahrenheit", id="c_to_f")
        yield Input(placeholder="Enter Fahrenheit (e.g., 212)", id="fahrenheit_input")
        yield Button("Convert to Celsius", id="f_to_c")
        yield Static("", id="result")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        result_widget = self.query_one("#result", Static)
        if event.button.id == "c_to_f":
            c_input = self.query_one("#celsius_input", Input).value
            try:
                c = float(c_input)
                f = (c * 9 / 5) + 32
                result_widget.update(f"✅ {c:.2f}°C = {f:.2f}°F")
            except ValueError:
                result_widget.update("❌ Please enter a valid number for Celsius.")
        elif event.button.id == "f_to_c":
            f_input = self.query_one("#fahrenheit_input", Input).value
            try:
                f = float(f_input)
                c = (f - 32) * 5 / 9
                result_widget.update(f"✅ {f:.2f}°F = {c:.2f}°C")
            except ValueError:
                result_widget.update("❌ Please enter a valid number for Fahrenheit.")

if __name__ == "__main__":
    app = TemperatureApp()
    app.run()
