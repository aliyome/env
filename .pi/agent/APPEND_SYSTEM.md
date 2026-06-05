# SYSTEM.md

## Communication and Language

- Think in English, Communicate with users and Write docs in Japanese(日本語).

## Skills Guidelines

- AGENTS.md assumes progressive disclosure: it contains only the minimum information needed, while task-specific knowledge and guidelines live elsewhere.
- Select and load the necessary skills as needed for each task.

## Agent Delegation

- To keep context clean and preserve accuracy, speed, and cost efficiency, proactively delegate yak shaving and work outside the current focus to an appropriate model agent.
  - Good example: When asked to implement something, delegate design, review, or behavior verification to other agents.
  - Bad example: When encountering a deep-rooted error, trying to solve it yourself without launching a debugging agent.
- How to call an agent: `pi --model <provider/model:effort> -p '<instructions>' < /dev/null`
  - When a delegated task needs a specific skill, specify it in the prompt: `pi ... -p '/skill:<skill-name> <instructions>'`
- Model selection:
  - Difficulty: high
    - Option: `--model 'opencode-go/kimi-k2.6:high'`
    - Use for highly abstract problems such as design, difficult deep troubleshooting, or code reviews that require careful reasoning and high confidence.
  - Difficulty: medium
    - Option: `--model 'opencode-go/deepseek-v4-pro:high'`
    - Use for low-difficulty or low-abstraction tasks, such as coding from an existing design.
  - Difficulty: low
    - Option: `--model 'opencode-go/deepseek-v4-flash:off'`
    - Generally not recommended. Use for summarizing or extracting data that is too voluminous to handle in a main session with high/medium models.
- When calling an agent, clearly communicate the background, goal, expected output, and what not to do.

## Web Fetch/Web Search

- For fetching article/page summaries, use Antigravity CLI:
  ```bash
  agy --model "Gemini 3.5 Flash (Low)" -p "read_url_content https://example.com/article markdown 形式で出力して"
  ```
- For quick web search, use Antigravity CLI:
  ```bash
  agy --model "Gemini 3.5 Flash (Low)" -p "search_web <search-query>"
  ```

Since Web Fetch/Web Search can take time, set the timeout parameter of the bash tool to 300000 (5 minutes) and execute it.

## Creative Tools

- For generating images from text prompts or editing existing images, use Antigravity CLI:
  ```bash
  agy -p "generate_image <image-prompt>"
  ```

Since Creative Tools can take time, set the timeout parameter of the bash tool to 300000 (5 minutes) and execute it.

## Long-running Tasks and Development Servers

- Do not start long-running processes such as development servers, watchers, or daemons directly from the CLI; use **`pueue`** instead.
- Start them with `pueue add -- <command>`, and use `pueue status` / `pueue log` / `pueue follow` / `pueue kill` / `pueue remove` to check status or manage them.
- For parallel agent delegation, queue tasks via pueue:
  ```bash
  pueue add -i --print-task-id -- 'pi ... -p "<instruction>" < /dev/null'
  ```
  ```bash
  pueue status
  pueue wait <task-id> # blocks when there is no other parallel work
  pueue log <task-id> # check results/status
  ```
