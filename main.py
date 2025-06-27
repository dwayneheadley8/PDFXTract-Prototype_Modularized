#!/usr/bin/env python3
"""
PDF Data Extractor
Main entry point that orchestrates the entire PDF processing pipeline.
"""

import sys
from config import PDF_FILE
from pdf_reader import read_pdf_text
from ai_extractor import extract_fields_with_timeout
from sheets_writer import save_or_upload_data

def main():
    """
    Main execution function that coordinates the entire process.
    """
    print("🚀 Starting PDF Data Extraction Pipeline...")
    print("=" * 50)
    
    # Step 1: Read PDF
    print("📄 Reading PDF...")
    text = read_pdf_text(PDF_FILE)
    
    if not text:
        print("❌ No text extracted from PDF. Exiting.")
        sys.exit(1)
    
    print(f"📝 Extracted {len(text)} characters from PDF")
    
    # Step 2: Extract fields with AI
    extracted_data = extract_fields_with_timeout(text)
    
    if extracted_data is None:
        print("❌ Field extraction failed. Exiting.")
        sys.exit(1)
    
    # Step 3: Save or upload data
    print("\n📊 Processing extracted data...")
    save_or_upload_data(extracted_data)
    
    print("\n✅ Pipeline completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error in main: {e}")
        sys.exit(1)
