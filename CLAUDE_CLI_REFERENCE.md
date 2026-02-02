# Claude Code CLI Reference

Quick reference for Claude Code command-line options.

## Permission Flags

| Flag | Description |
|------|-------------|
| `--dangerously-skip-permissions` | Bypass ALL permission checks. Use only in trusted sandboxes. |
| `--allow-dangerously-skip-permissions` | Enable the skip option without auto-activating it. |
| `--permission-mode <mode>` | Set permission mode: `acceptEdits`, `bypassPermissions`, `default`, `delegate`, `dontAsk`, `plan` |

## Tool Control

| Flag | Description |
|------|-------------|
| `--allowedTools <tools>` | Comma/space-separated list of allowed tools (e.g., `"Bash(git:*) Edit"`) |
| `--disallowedTools <tools>` | Comma/space-separated list of denied tools |
| `--tools <tools>` | Specify available tools: `""` (none), `"default"` (all), or specific names |

### Tool Name Examples
```
Bash(python:*)      # Allow all python commands
Bash(npm:*)         # Allow all npm commands
Bash(git:*)         # Allow all git commands
Edit                # Allow file editing
Read                # Allow file reading
Write               # Allow file writing
WebFetch            # Allow web requests
```

## Session Management

| Flag | Description |
|------|-------------|
| `-c, --continue` | Continue most recent conversation |
| `-r, --resume [id]` | Resume by session ID or open picker |
| `--session-id <uuid>` | Use specific session ID |
| `--fork-session` | Create new session ID when resuming |
| `--no-session-persistence` | Don't save session to disk |

## Model Selection

| Flag | Description |
|------|-------------|
| `--model <model>` | Set model: `sonnet`, `opus`, `haiku`, or full name |
| `--fallback-model <model>` | Fallback when primary is overloaded |

## Output Modes

| Flag | Description |
|------|-------------|
| `-p, --print` | Print response and exit (non-interactive) |
| `--output-format <format>` | `text` (default), `json`, `stream-json` |
| `--input-format <format>` | `text` (default), `stream-json` |
| `--json-schema <schema>` | Enforce structured JSON output |

## System Prompts

| Flag | Description |
|------|-------------|
| `--system-prompt <prompt>` | Override system prompt |
| `--append-system-prompt <prompt>` | Add to default system prompt |

## MCP Servers

| Flag | Description |
|------|-------------|
| `--mcp-config <configs>` | Load MCP servers from JSON files |
| `--strict-mcp-config` | Only use MCP servers from --mcp-config |

## Directories & Files

| Flag | Description |
|------|-------------|
| `--add-dir <dirs>` | Additional directories for tool access |
| `--file <specs>` | Download files at startup (format: `file_id:path`) |
| `--settings <file>` | Load settings from JSON file |

## Debug & Development

| Flag | Description |
|------|-------------|
| `-d, --debug [filter]` | Enable debug mode (e.g., `"api,hooks"`) |
| `--debug-file <path>` | Write debug logs to file |
| `-v, --version` | Show version |
| `-h, --help` | Show help |

## Budget Control

| Flag | Description |
|------|-------------|
| `--max-budget-usd <amount>` | Max spend on API calls (with --print) |

## Plugins & Skills

| Flag | Description |
|------|-------------|
| `--plugin-dir <paths>` | Load plugins from directories |
| `--disable-slash-commands` | Disable all skills |

## Custom Agents

| Flag | Description |
|------|-------------|
| `--agent <agent>` | Set agent for session |
| `--agents <json>` | Define custom agents as JSON |

### Agent JSON Example
```json
{
  "reviewer": {
    "description": "Reviews code",
    "prompt": "You are a code reviewer"
  }
}
```

---

## GitHub Action Usage

In `.github/workflows/claude.yml`:

```yaml
- name: Run Claude
  uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    claude_args: "--dangerously-skip-permissions"
```

### Available Action Inputs

| Input | Description |
|-------|-------------|
| `anthropic_api_key` | API key for authentication |
| `claude_code_oauth_token` | OAuth token (alternative to API key) |
| `claude_args` | Additional CLI arguments |
| `prompt` | Custom instructions for Claude |
| `settings` | Settings JSON or file path |
| `trigger_phrase` | Trigger phrase (default: `@claude`) |
| `allowed_bots` | Comma-separated bot usernames, or `*` for all |

---

## Common Examples

### Skip all permissions (dangerous)
```bash
claude --dangerously-skip-permissions "create a file"
```

### Allow specific bash commands
```bash
claude --allowedTools "Bash(python:*),Bash(npm:*)" "run tests"
```

### Non-interactive with JSON output
```bash
claude -p --output-format json "what is 2+2"
```

### Continue last session
```bash
claude -c
```

### Use specific model
```bash
claude --model opus "complex task"
```

### Set budget limit
```bash
claude -p --max-budget-usd 5.00 "analyze codebase"
```
