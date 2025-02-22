import typer

from rich.console import Console
from rich.text import Text

import json
import random


# Create a Typer app instance
app = typer.Typer()

# Create a Rich Console instance for pretty output
console = Console()

# Load quotes
def load_quotes(file_path="quotes.json"):
    try:
        with open(file_path, "r") as file:
            quotes = json.load(file)
    except FileNotFoundError:
        print("[bold red]Error: quotes.json not found![/bold red]")
        return [{"text": "No quotes available.", "author": "Unknown"}]
    except json.JSONDecodeError:
        print("[bold red]Error: Invalid JSON format in quotes.json![/bold red]")
        return [{"text": "No quotes available.", "author": "Unknown"}]
    return quotes

# Display quote
def display_quote(quotes):
    quote = random.choice(quotes)
    #content = quote['text']
    content = f"[italic cyan]\"{quote['text']}\"[/italic cyan]\n\n- [bold yellow]{quote['author']}[/bold yellow]"
    console.print(content)

# Save qvote
def save_quotes(quotes):
    with open(file_path, "w") as file:
        json.dump(quotes, file, indent=4)  # Pretty print with indent


file_path="quotes.json"
quotes = load_quotes()
    
# Main
@app.command("q")
def quote():
    display_quote(quotes)

# Listen
@app.command("l")
def listen():
    console.print("[italic cyan] I'm listening [/italic cyan]")
    text = input("Quote text: ").strip()
    if not text:
        console.print("[bold red]Wasting my time![/bold red]")
        return
    new_quote = {"text": text, "author": "Rumha"}
    quotes.append(new_quote)
    save_quotes(quotes)
    console.print("[italic cyan]Smart...[/italic cyan]")


if __name__ == "__main__":
    app()