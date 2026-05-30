# Streamlit Cloud deployment fix

The deployment error occurs when `requirements.txt` contains HTML. Streamlit Cloud runs `pip install -r requirements.txt`, so this file must contain Python package requirements only.

Correct `requirements.txt`:

```txt
streamlit>=1.36.0
```

Keep the portfolio HTML in `index.html`, not in `requirements.txt`.

Recommended repository root:

```text
portfolio_streamlit/
├── app.py
├── index.html
├── requirements.txt
├── .python-version
├── .streamlit/
│   └── config.toml
└── assets/
    └── GM_Full.png
```
