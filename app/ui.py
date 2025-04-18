from fasthtml.common import *
from app.logic import summarize
from IPython.display import Markdown

app, rt = fast_app()

@rt("/")
def get():
    return HTMLResponse(
        """
        <html>
        <head>
        <style>
            body {
                background-color: #ffe6f0;
                font-family: Arial, sans-serif;
                padding: 2em;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 2em;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            input[type=text] {
                width: 100%;
                padding: 10px;
                margin-bottom: 1em;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                background-color: #ff80ab;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .summary {
                margin-top: 2em;
                white-space: pre-wrap;
            }
        </style>
        </head>
        <body>
            <div class="container">
                <h2>Website Summarizer</h2>
                <form hx-post="/summarize" hx-target="#summary" hx-swap="innerHTML">
                    <input type="text" name="url" placeholder="Enter a website URL..." required />
                    <button type="submit">Summarize</button>
                </form>
                <div id="summary" class="summary"></div>
            </div>
        </body>
        </html>
        """
    )

@rt("/summarize", methods=["POST"])
def summarize_handler(url: str):
    try:
        result = summarize(url)
        return Markdown(result)
    except Exception as e:
        return Div(P(f"Error summarizing: {str(e)}"))

serve()