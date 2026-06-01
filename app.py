from pathlib import Path
import base64
import mimetypes

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).resolve().parent
HTML_PATH = APP_DIR / "index.html"
PHOTO_PATH = APP_DIR / "assets" / "GM_Full.png"


def to_data_uri(path: Path) -> str:
    """Return a browser-safe data URI for a local asset."""
    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def load_portfolio_html() -> str:
    """Load the original portfolio HTML and inject the local portrait image."""
    html = HTML_PATH.read_text(encoding="utf-8")
    photo_uri = to_data_uri(PHOTO_PATH)

    # The source HTML/CSS/layout is intentionally preserved. Only the local image
    # reference is replaced so the portfolio works on Streamlit Cloud and GitHub clones.
    html = html.replace('src="assets/GM_Full.png"', f'src="{photo_uri}"')
    return html


st.set_page_config(
    page_title="Ghulam Murtaza | Professional Portfolio",
    page_icon="GM",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"] {
        margin: 0 !important;
        padding: 0 !important;
        background: #f8fafc !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"], footer, #MainMenu {
        display: none !important;
        visibility: hidden !important;
      }
      .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }
      iframe {
        display: block !important;
        width: 100% !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(load_portfolio_html(), height=4400, scrolling=True)
