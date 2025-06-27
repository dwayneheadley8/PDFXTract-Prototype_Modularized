import re
import json
import concurrent.futures
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from config import GITHUB_TOKEN, AI_ENDPOINT, AI_TEMPERATURE, AI_TOP_P, AI_MAX_TOKENS, AI_MODEL, AI_TIMEOUT

# === AI CLIENT SETUP ===
client = ChatCompletionsClient(
    endpoint=AI_ENDPOINT,
    credential=AzureKeyCredential(GITHUB_TOKEN),
)

def extract_fields_with_ai(text):
    """
    Extract structured fields from text using AI.
    
    Args:
        text (str): Text to extract fields from
        
    Returns:
        str: AI response containing extracted fields, or None if error
    """
    prompt = f"""
You are an AI assistant. Extract the following fields from the text below if present:
Full Name, Client ID, Date, Phone, Email, DOB.
Return the output as a JSON object with keys exactly as these fields.
If a field is missing, use null as the value.

Text:
\"\"\"{text}\"\"\"
"""
    try:
        print("🔄 Making API request to Llama...")
        response = client.complete(
            messages=[
                SystemMessage(content="You are a helpful assistant that extracts structured client information."),
                UserMessage(content=prompt),
            ],
            temperature=AI_TEMPERATURE,
            top_p=AI_TOP_P,
            max_tokens=AI_MAX_TOKENS,
            model=AI_MODEL,
        )
        print("✅ AI response received successfully!")
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Error calling AI API: {e}")
        print("🔍 Debug info:")
        print(f"   - Token length: {len(GITHUB_TOKEN) if GITHUB_TOKEN else 0}")
        print(f"   - Text length: {len(text)}")
        return None

def clean_json_string(raw):
    """
    Extract JSON object from AI response string.
    
    Args:
        raw (str): Raw AI response
        
    Returns:
        str: Cleaned JSON string
    """
    # Use regex to extract the first JSON object from the string
    match = re.search(r'\{[\s\S]*?\}', raw)
    if match:
        return match.group(0)
    return ""

def extract_fields_with_timeout(text):
    """
    Extract fields with timeout protection using process pool.
    
    Args:
        text (str): Text to extract fields from
        
    Returns:
        dict: Parsed JSON data or None if error/timeout
    """
    print("🤖 Sending to AI...")
    print(f"⏰ Enforcing {AI_TIMEOUT}-second timeout for AI processing (process-based)...")
    
    raw_response = None
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future = executor.submit(extract_fields_with_ai, text)
            raw_response = future.result(timeout=AI_TIMEOUT)
    except concurrent.futures.TimeoutError:
        print("⏰ Timeout reached! AI processing took too long.")
        return None
    except KeyboardInterrupt:
        print("\n⏹️ Process interrupted by user")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

    if raw_response is None:
        print("❌ AI processing failed.")
        return None

    print("🧠 AI Response:")
    print(raw_response)

    try:
        cleaned = clean_json_string(raw_response)
        print("Cleaned JSON string:", cleaned)
        parsed = json.loads(cleaned)
        print("Parsed dict keys:", list(parsed.keys()))
        print("✅ JSON parsed successfully")
        return parsed
    except Exception as e:
        print("⚠️ Error parsing JSON response:", e)
        return None
