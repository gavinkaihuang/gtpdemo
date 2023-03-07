curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: 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" \
-d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'