import os
import json
import gspread
from google.oauth2.service_account import Credentials
from config import CREDENTIALS_FILE, GOOGLE_SHEET_ID

def get_flexible(data, *keys):
    """
    Get value from dictionary using multiple possible keys.
    
    Args:
        data (dict): Dictionary to search
        *keys: Possible keys to look for
        
    Returns:
        Any: Value found or empty string if not found
    """
    for key in keys:
        if key in data:
            return data[key]
    return ""

def safe_str(val):
    """
    Safely convert value to string.
    
    Args:
        val: Value to convert
        
    Returns:
        str: String representation of value
    """
    if isinstance(val, list):
        return ", ".join(str(x) for x in val)
    return str(val) if val is not None else ""

def append_to_google_sheet(data_dict):
    """
    Append extracted data to Google Sheet.
    
    Args:
        data_dict (dict): Dictionary containing extracted field data
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1

        row = [
            safe_str(get_flexible(data_dict, "Full Name", "Name")),
            safe_str(get_flexible(data_dict, "Phone", "Contact", "Contact #")),
            safe_str(get_flexible(data_dict, "Date")),
            safe_str(get_flexible(data_dict, "Email", "E-mail")),
        ]
        print("Row to append:", row)
        print("Data dict keys:", list(data_dict.keys()))
        sheet.append_row(row)
        print("✅ Data written to Google Sheet successfully.")
        return True
    except Exception as e:
        print(f"❌ Error writing to Google Sheet: {e}")
        return False

def save_or_upload_data(data_dict):
    """
    Save data to Google Sheets or print to console if credentials not available.
    
    Args:
        data_dict (dict): Dictionary containing extracted field data
    """
    # Check if credentials file exists before trying to upload
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"⚠️ Google credentials file '{CREDENTIALS_FILE}' not found. Skipping Google Sheets upload.")
        print("📋 Extracted data:")
        print(json.dumps(data_dict, indent=2))
    else:
        append_to_google_sheet(data_dict)
