# 🔍 PDFXTract-Prototype_Modularized

📄 **AI-Powered PDF Data Extraction Pipeline** - *Modularized Edition*

> 🚀 **This is an updated, modularized version** of the original monolithic PDF extraction prototype, now with improved architecture and maintainability!

## ✨ Features

- 📖 **PDF Text Extraction**: Extract text from PDF forms using PyMuPDF
- 🤖 **AI-Powered Data Extraction**: Uses Llama models via GitHub Models API
- 📊 **Google Sheets Integration**: Automatically uploads structured data
- ⚡ **Robust Error Handling**: Comprehensive timeout protection and error management
- 🏗️ **Modular Architecture**: Clean separation of concerns for better maintainability
- 🔄 **Concurrent Processing**: Process-based timeout management for reliability

## 🏛️ Architecture

```
📦 PDFXTract-Prototype_Modularized/
├── 🚀 main.py                    # Entry point - orchestrates the pipeline
├── 📄 pdf_reader.py             # PDF text extraction module
├── 🧠 ai_extractor.py           # AI communication and response parsing
├── 📊 sheets_writer.py          # Google Sheets integration
├── ⚙️ config.py                 # Configuration management
├── 📋 sample_form2.pdf          # Test PDF file
└── 📖 README.md                 # This file
```

## 🛠️ Installation

### 1. Install Dependencies
```bash
pip install PyMuPDF gspread google-auth azure-ai-inference
```

### 2. Set up Google Sheets API 🔑
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project or select existing one
- Enable Google Sheets API
- Create service account credentials
- Download `credentials.json` and place in project directory

### 3. Configure GitHub Models API 🔐
- Get your GitHub token from [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
- Update `GITHUB_TOKEN` in `config.py`

### 4. Set up Google Sheet 📊
- Create a new Google Sheet
- Share it with your service account email
- Update `GOOGLE_SHEET_ID` in `config.py`

## 🚀 Usage

1. **Configure your settings** in `config.py`:
   ```python
   GITHUB_TOKEN = "your_github_token_here"
   GOOGLE_SHEET_ID = "your_google_sheet_id_here"
   PDF_FILE = "your_pdf_file.pdf"
   ```

2. **Place your PDF** in the project directory

3. **Run the pipeline**:
   ```bash
   python main.py
   ```

## 📋 Extracted Fields

The AI intelligently extracts these fields from PDF forms:
- 👤 **Full Name**
- 🆔 **Client ID** 
- 📅 **Date**
- 📞 **Phone**
- 📧 **Email**
- 🎂 **Date of Birth (DOB)**

## 🔧 Configuration

All settings are centralized in `config.py`:

```python
# API Configuration
GITHUB_TOKEN = "your_token_here"
GOOGLE_SHEET_ID = "your_google_sheet_id_here"

# File Paths
PDF_FILE = "sample_form2.pdf"
CREDENTIALS_FILE = "credentials.json"

# AI Model Settings
AI_MODEL = "meta/Llama-4-Scout-17B-16E-Instruct"
AI_TIMEOUT = 60  # seconds
```

## 🛡️ Error Handling

- 📄 **PDF Reading**: Handles corrupted or empty PDFs gracefully
- ⏱️ **API Timeout**: 60-second timeout protection with process isolation
- 🧩 **JSON Parsing**: Robust extraction of structured data from AI responses
- 📊 **Google Sheets**: Fallback to console output if credentials unavailable
- 🔄 **Process Management**: Graceful handling of interruptions and errors

## 📦 Dependencies

| Package | Purpose |
|---------|----------|
| `PyMuPDF` | PDF text extraction |
| `gspread` | Google Sheets API client |
| `google-auth` | Google authentication |
| `azure-ai-inference` | GitHub Models API client |
| `concurrent.futures` | Process-based timeout management |

## 🆕 What's New in This Version?

✅ **Modular Architecture**: Separated concerns into focused modules  
✅ **Centralized Configuration**: All settings in one place  
✅ **Better Error Handling**: More robust error management  
✅ **Improved Maintainability**: Clean, documented code structure  
✅ **Enhanced User Experience**: Better progress feedback and status updates  

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| 📄 PDF not reading | Check file exists and isn't corrupted |
| 🤖 AI API errors | Verify GitHub token and internet connection |
| 📊 Google Sheets errors | Check credentials and sheet permissions |
| ⏱️ Timeout issues | Increase `AI_TIMEOUT` in config.py |
| 🔑 Missing credentials | Ensure `credentials.json` is in project directory |

## 📝 License

This project is for educational and prototyping purposes.

---

💡 **Tip**: This modularized version makes it easy to swap out components (like switching from Google Sheets to a database) without touching the core logic!

🔗 **Upgrade from Monolithic**: This version refactors the original single-file approach into a clean, maintainable modular architecture.
