# === CONFIGURATION ===
# TODO: Set your GitHub model API key
GITHUB_TOKEN = "your_github_token_here"  # GitHub model API key
PDF_FILE = "sample_form2.pdf"  # Your PDF file
CREDENTIALS_FILE = "credentials.json"  # Google credentials
# TODO: Set your Google Sheet ID
GOOGLE_SHEET_ID = "your_google_sheet_id_here"  # Google Sheet ID

# AI Model Configuration
AI_TEMPERATURE = 0
AI_TOP_P = 1
AI_MAX_TOKENS = 500
AI_MODEL = "meta/Llama-4-Scout-17B-16E-Instruct"
AI_TIMEOUT = 60  # seconds

# AI Client Endpoint
AI_ENDPOINT = "https://models.github.ai/inference"
