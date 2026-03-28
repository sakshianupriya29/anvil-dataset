# Task: Mini URL Shortener

You are building a simple URL shortener system.

Functions:

1. shorten(url)
2. resolve(short_code)

Rules:

1. Each new URL gets a unique short code
2. If same URL is shortened again → return same code
3. Codes should be incremental (1, 2, 3, ...)
4. resolve(code) should return original URL
5. If code not found → return None

Example:

shorten("google.com") → "1"
shorten("openai.com") → "2"
shorten("google.com") → "1"

resolve("1") → "google.com"
resolve("3") → None