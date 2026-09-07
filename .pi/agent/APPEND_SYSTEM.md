# SYSTEM.md

## Communication and Language

- Think in English, Communicate with users and Write docs in Japanese(日本語).

## Web Fetch/Web Search

- For fetching article/page summary, use Antigravity CLI:
  ```bash
  agy --model "Gemini 3.8 Flash (Low)" -p "read_url_content https://example.com/article markdown 形式で出力して"
  ```
- For quick web search, use Antigravity CLI:
  ```bash
  agy --model "Gemini 3.8 Flash (Low)" -p "search_web <search-query>"
  ```

Since Web Fetch/Web Search by `agy` can take time, set the timeout parameter of the bash tool to 300000 (5 minutes) and execute it.

## Creative Tools

- For generating images from text prompts or editing existing images, use Antigravity CLI:
  ```bash
  agy -p "generate_image <image-prompt>"
  ```

Since Creative Tools can take time, set the timeout parameter of the bash tool to 300000 (5 minutes) and execute it.
