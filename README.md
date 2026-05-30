# Ghulam Murtaza Streamlit Portfolio

This repository converts the supplied one-page HTML portfolio into a Streamlit app while preserving the original HTML structure, CSS styling, layout, and element positioning.

## Repository Structure

```text
.
├── app.py
├── index.html
├── requirements.txt
├── assets/
│   └── GM_Full.png
└── .streamlit/
    └── config.toml
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Upload this repository to GitHub.
2. Open Streamlit Community Cloud.
3. Select the GitHub repository.
4. Set the main file path to:

```text
app.py
```

5. Deploy.

## Implementation Notes

- The original HTML is stored in `index.html`.
- The portrait image is stored in `assets/GM_Full.png`.
- `app.py` renders the HTML through `streamlit.components.v1.html` to preserve the page styling and structure.
- The local image path from the HTML was replaced with a repo-relative path, then injected as a data URI at runtime so it works reliably in Streamlit deployments.
- External social icons are still loaded from their original external URLs.
