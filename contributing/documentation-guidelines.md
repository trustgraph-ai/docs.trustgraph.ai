---
title: Documentation Guidelines
parent: Contributing
review_date: 2026-05-24
---

# Documentation Guidelines

This guide defines standards for writing and maintaining TrustGraph documentation, with a focus on CLI command reference documentation.

## CLI Command Documentation

### Purpose

CLI reference documentation should be **concise, task-focused, and administrative** in nature. These are reference documents, not tutorials or scripting guides.

### Target Length by Command Complexity

| Command Type | Target Length | Characteristics |
|-------------|---------------|-----------------|
| **Simple** | <150 lines | Single operation, few options (e.g., `tg-list-collections`) |
| **Medium** | 150-250 lines | Multiple options or modes (e.g., `tg-invoke-agent`) |
| **Complex** | 250-400 lines | Multi-mode operations, complex workflows (e.g., `tg-load-structured-data`) |

Commands exceeding these targets should be reviewed for unnecessary content.

### Required Sections

Every CLI command document must include:

1. **Front Matter** (YAML)
   ```yaml
   ---
   title: command-name
   parent: CLI
   review_date: YYYY-MM-DD
   ---
   ```

2. **Title and One-line Description**
   ```markdown
   # command-name

   Brief description of what the command does.
   ```

3. **Synopsis**
   ```markdown
   ## Synopsis

   \`\`\`bash
   command-name [required-args] [options]
   \`\`\`
   ```

4. **Description**
   - Clear explanation of command purpose (2-4 sentences)
   - Important caveats or limitations in **bold**
   - Use cases (1-2 sentences)

5. **Options**
   - Use tables for clarity
   - Separate Required and Optional arguments
   - Include defaults where applicable

   ```markdown
   ### Required Arguments

   | Option | Description |
   |--------|-------------|
   | `--option ARG` | What it does |

   ### Optional Arguments

   | Option | Default | Description |
   |--------|---------|-------------|
   | `-u, --url URL` | `$VAR` or `http://...` | What it does |
   ```

6. **Examples** (2-4 focused examples)
   - Each example should be ≤10 lines (ideally 1-3 lines)
   - Examples should illustrate features of the command, not the shell environment
   - Don't teach bash scripting (loops, conditionals, functions) in command reference docs
   - Show common use cases only
   - Use realistic but simple values

7. **Environment Variables** (if applicable)
   - List relevant environment variables
   - Brief description of each

8. **Related Commands**
   - 3-5 most relevant related commands
   - Include brief description of each
   - Use relative links: `[command-name](command-name)`

9. **API Integration** (if applicable)
   - Single sentence stating which API the command uses
   - Link to API documentation

### Optional Sections

Include only when genuinely necessary:

- **Notes**: Important information that doesn't fit elsewhere (1-3 bullet points)
- **Output Format**: When output structure is complex or non-obvious
- **Error Messages**: Only common/important errors with brief solutions

### What NOT to Include

**Do not include** in CLI reference documentation:

1. **Complex Bash Scripts**
   - No functions longer than 10 lines
   - No elaborate monitoring/processing workflows
   - No CSV exporters, parallel processors, or automation frameworks

2. **Redundant Examples**
   - Avoid multiple examples showing the same pattern
   - Don't include variations that differ only in parameter values

3. **Generic Sections**
   - "Best Practices" applicable to all commands
   - Generic troubleshooting (API connection issues, permission errors)
   - Verbose "What It Does" vs "What It Doesn't Do" lists

4. **Advanced Usage Sections**
   - Unless the command genuinely has complex modes
   - Complex workflows belong in tutorials/guides, not reference docs

5. **Hypothetical Examples**
   - Examples requiring non-existent APIs
   - Placeholder implementations
   - "This would require..." comments

### Style Guidelines

**Language:**
- Use imperative mood for descriptions ("Removes", "Creates", "Lists")
- Be direct and concise
- Avoid marketing language and superlatives

**Formatting:**
- Use tables for options (more scannable than lists)
- Use code blocks for all commands
- Use **bold** for important warnings/caveats
- Use `inline code` for command names, options, file paths, values

**Examples:**
- Always include the command name in examples
- Show realistic but simple values
- Avoid overly complex scenarios
- Each example should demonstrate a distinct use case
- Focus on the command's features, not shell scripting techniques
- If users need to run the command multiple times, just show it once

### Example: Good vs Bloated

**Good (85 lines):**
```markdown
# tg-stop-library-processing

Removes a library document processing record.

## Synopsis
...

## Description
Brief explanation with important caveat.

## Options
Table of 2-3 options

## Examples (3 examples, each ≤5 lines)
...

## Related Commands
...
```

**Bloated (514 lines):**
- 10+ bash script examples with functions
- "Safe processing cleanup" workflows
- Age-based cleanup scripts
- Bulk verification processors
- Generic troubleshooting section
- Generic best practices section

## General Documentation Standards

### All Documentation

1. **Clarity First**: Write for users who need quick answers
2. **Structure**: Use consistent heading hierarchy
3. **Links**: Always verify internal links work
4. **Code Examples**: Test all code examples when possible
5. **Review Dates**: Update `review_date` when making significant changes

### Voice and Tone

- Professional and direct
- Task-oriented
- No unnecessary verbosity
- Avoid phrases like "simply", "just", "easy"

### Maintenance

- Review CLI docs annually (check `review_date`)
- Update examples when APIs change
- Remove outdated information promptly
- Keep line counts within target ranges

## Review Checklist

Before submitting CLI documentation:

- [ ] Meets target length for command complexity
- [ ] All required sections present
- [ ] No bash scripts >10 lines
- [ ] Examples are focused and realistic
- [ ] No hypothetical/placeholder examples
- [ ] No generic troubleshooting
- [ ] Tables used for options
- [ ] Related commands included
- [ ] Review date set
- [ ] Links verified

## Questions?

See [Contributing Guidelines](contributing) for how to contribute documentation improvements.
