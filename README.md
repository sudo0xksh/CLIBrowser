# 🧠 CLI Browser – Because Real Browsers Are Too Mainstream

Welcome to **CLI Browser**, a Python-based command-line browser for people who:
- Hate opening Chrome
- Love staring at raw HTML
- Think terminals are personality traits

This tool lets you fetch any website directly from your terminal and prints:
- Target URL
- HTTP status code
- Entire response body (yes, the whole thing 😈)

---

## 🗿 Why This Exists

Because sometimes you don’t want:
❌ Tabs  
❌ Ads  
❌ RAM usage  

You want:
✅ Chaos  
✅ Raw HTML  
✅ Terminal dominance  

Also because every hacker journey starts with printing HTML in terminal and feeling powerful.

---

## ⚙️ How It Works (High IQ Explanation)

1. Takes a URL as a command-line argument  
2. Sends an HTTP GET request using `requests`  
3. Displays:
   - Target URL
   - HTTP status code
   - Full response text  
4. Exits politely like a well-mannered script

That’s it. No cookies. No JavaScript. No feelings.

---

## 🧪 Usage

```bash
python cli_browser.py https://example.com
