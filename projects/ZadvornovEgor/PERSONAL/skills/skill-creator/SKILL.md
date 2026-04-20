---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific
domains or tasks - they transform Claude from a general-purpose agent into a specialized agent
equipped with procedural knowledge that no model can fully possess.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

### Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
  SKILL.md (required)
    YAML frontmatter metadata (required)
      name: (required)
      description: (required)
    Markdown instructions (required)
  Bundled Resources (optional)
    scripts/          - Executable code (Python/Bash/etc.)
    references/       - Documentation intended to be loaded into context as needed
    assets/           - Files used in output (templates, icons, fonts, etc.)
```

#### SKILL.md (required)

**Metadata Quality:** The `name` and `description` in YAML frontmatter determine when Claude will use the skill. Be specific about what the skill does and when to use it. Use the third-person (e.g. "This skill should be used when..." instead of "Use this skill when...").

#### Bundled Resources (optional)

##### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by Claude for patching or environment-specific adjustments

##### References (`references/`)

Documentation and reference material intended to be loaded as needed into context to inform Claude's process and thinking.

- **When to include**: For documentation that Claude should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/api_docs.md` for API specifications
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when Claude determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill - this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

##### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output Claude produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified
- **Benefits**: Separates output resources from documentation, enables Claude to use files without loading them into context

### Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude (Unlimited*)

*Unlimited because scripts can be executed without reading into context window.

## Skill Creation Process

To create a skill, follow the "Skill Creation Process" in order, skipping steps only if there is a clear reason why they are not applicable.

### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

For example, when building an image-editor skill, relevant questions include:

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

Conclude this step when there is a clear sense of the functionality the skill should support.

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Example: When building a `pdf-editor` skill to handle queries like "Help me rotate this PDF," the analysis shows:

1. Rotating a PDF requires re-writing the same code each time
2. A `scripts/rotate_pdf.py` script would be helpful to store in the skill

Example: When designing a `frontend-webapp-builder` skill for queries like "Build me a todo app" or "Build me a dashboard to track my steps," the analysis shows:

1. Writing a frontend webapp requires the same boilerplate HTML/React each time
2. An `assets/hello-world/` template containing the boilerplate HTML/React project files would be helpful to store in the skill

Example: When building a `big-query` skill to handle queries like "How many users have logged in today?" the analysis shows:

1. Querying BigQuery requires re-discovering the table schemas and relationships each time
2. A `references/schema.md` file documenting the table schemas would be helpful to store in the skill

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

### Step 3: Initializing the Skill

At this point, it is time to actually create the skill.

Skip this step only if the skill being developed already exists, and iteration or packaging is needed. In this case, continue to the next step.

When creating a new skill from scratch, always run the `init_skill.py` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

Usage:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

The script:

- Creates the skill directory at the specified path
- Generates a SKILL.md template with proper frontmatter and TODO placeholders
- Creates example resource directories: `scripts/`, `references/`, and `assets/`
- Adds example files in each directory that can be customized or deleted

After initialization, customize or remove the generated SKILL.md and example files as needed.

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of Claude to use. Focus on including information that would be beneficial and non-obvious to Claude. Consider what procedural knowledge, domain-specific details, or reusable assets would help another Claude instance execute these tasks more effectively.

#### Start with Reusable Skill Contents

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

Also, delete any example files and directories not needed for the skill. The initialization script creates example files in `scripts/`, `references/`, and `assets/` to demonstrate structure, but most skills won't need all of them.

#### Update SKILL.md

**Writing Style:** Write the entire skill using **imperative/infinitive form** (verb-first instructions), not second person. Use objective, instructional language (e.g., "To accomplish X, do Y" rather than "You should do X" or "If you need to do X"). This maintains consistency and clarity for AI consumption.

To complete SKILL.md, answer the following questions:

1. What is the purpose of the skill, in a few sentences?
2. When should the skill be used?
3. In practice, how should Claude use the skill? All reusable skill contents developed above should be referenced so that Claude knows how to use them.

### Step 5: Packaging a Skill

Once the skill is ready, it should be packaged into a distributable zip file that gets shared with the user. The packaging process automatically validates the skill first to ensure it meets all requirements:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Optional output directory specification:

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

The packaging script will:

1. **Validate** the skill automatically, checking:
   - YAML frontmatter format and required fields
   - Skill naming conventions and directory structure
   - Description completeness and quality
   - File organization and resource references

2. **Package** the skill if validation passes, creating a zip file named after the skill (e.g., `my-skill.zip`) that includes all files and maintains the proper directory structure for distribution.

If validation fails, the script will report the errors and exit without creating a package. Fix any validation errors and run the packaging command again.

### Step 6: Register the Skill

After creating or packaging the skill, register it in the routing configuration so it gets auto-routed.

**Required:**
1. Add a routing entry mapping trigger words to the skill name
   ```
   | Category | "trigger1", "trigger2", "trigger3" | Skill `skill-name` |
   ```

### Step 7: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**
1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again

## Best Practices

### 1. Clear Naming

Use descriptive, unique names that clearly indicate the skill's purpose.

```yaml
# Good
name: git-workflow
description: Git operations - commits, branches, PRs, merge conflicts

# Bad
name: git-stuff
description: Git things
```

### 2. Specific Triggers

Define specific, actionable triggers that clearly indicate when the skill should be used.

```yaml
# Good - specific triggers
## When to Use
- Creating commit messages following Conventional Commits
- Resolving merge conflicts
- Setting up branch protection rules
- Squashing commits before merge

# Bad - vague triggers
## When to Use
- Git stuff
- When working with code
```

### 3. Actionable Instructions

Provide step-by-step instructions that are clear and actionable.

```yaml
# Good - step by step
## Creating a Release

1. Update version in package.json
2. Run `npm run changelog` to generate CHANGELOG
3. Create release commit: `git commit -m "chore: release v1.2.0"`
4. Tag the release: `git tag v1.2.0`
5. Push with tags: `git push --follow-tags`

# Bad - no steps
## Creating a Release
Make a release when ready
```

### 4. Code Examples

Include real, working code examples that demonstrate the skill's usage.

```yaml
# Good - real examples
## API Usage

```python
import requests

response = requests.post(
    "https://api.example.com/users",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"name": "John", "email": "john@example.com"}
)
user = response.json()
print(f"Created user: {user['id']}")
```

# Bad - pseudo-code
## API Usage
Call the API with your data
```

### 5. Error Handling

Document common errors and their solutions.

```yaml
## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Check API_KEY in .env |
| 429 Rate Limited | Too many requests | Add delay between calls |
| 500 Server Error | API issue | Retry with exponential backoff |
```

## Skill Template

Complete markdown template for creating new skills:

```markdown
---
name: [skill-name]
description: [One line description - when Claude should use this]
---

# [Skill Name]

## Overview

[2-3 sentences about what this skill does]

## When to Use

- [Specific trigger 1]
- [Specific trigger 2]
- [Specific trigger 3]

## Prerequisites

- [Requirement 1]
- [Requirement 2]

## Quick Start

```python
# Minimal working example
[code]
```

## Core Functions

### [Function 1]

[Description]

```python
[Code example]
```

### [Function 2]

[Description]

```python
[Code example]
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `VAR_1` | [Description] | [Value] |
| `VAR_2` | [Description] | [Value] |

## Common Patterns

### [Pattern 1]

[Description and example]

### [Pattern 2]

[Description and example]

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| [Error] | [Cause] | [Solution] |

## Integration Examples

### With [Other Tool/Skill]

[Example of combining skills]

## Tips

1. [Tip 1]
2. [Tip 2]
3. [Tip 3]

## References

- [Link 1]
- [Link 2]
```

## Skill Categories

### API Integration Skills

Focus on:
- Authentication methods
- Endpoint documentation
- Request/response examples
- Rate limiting
- Error codes

### Workflow Skills

Focus on:
- Step-by-step processes
- Decision trees
- Checklists
- Templates

### Tool Skills

Focus on:
- Installation
- CLI commands
- Configuration
- Common use cases

### Methodology Skills

Focus on:
- Principles
- Techniques
- When to apply
- Examples

## File Organization

Recommended directory structure for organizing skills:

```
skills/
  ai-models/           # AI API integrations
    openai.md
    anthropic.md
    gemini.md
  development/         # Dev tools & practices
    git-workflow.md
    tdd.md
    code-review.md
  business/           # Business processes
    invoicing.md
    leads.md
  automation/         # Automation tools
    n8n.md
    playwright.md
```

## Testing Your Skill

### Manual Test

1. Save skill to skills directory
2. Ask Claude: "[trigger phrase]"
3. Verify Claude uses the skill correctly
4. Check outputs match expectations

### Checklist

- [ ] Name is descriptive and unique
- [ ] Description fits in one line
- [ ] Triggers are specific
- [ ] Has working code examples
- [ ] Error cases documented
- [ ] No broken links
- [ ] Tested with Claude

## Updating Skills

### When to Update

- API changes
- New features discovered
- Bug fixes
- Better examples found
- User feedback

### Version Notes

Track changes using comments in the skill file:

```markdown
<!-- Changelog -->
<!-- v1.1 - Added rate limiting section -->
<!-- v1.0 - Initial version -->
```

## Common Mistakes

### Too Vague

```markdown
## When to Use
Use this for API stuff
```

### Specific

```markdown
## When to Use
- Generating API documentation from OpenAPI spec
- Creating Postman collections
- Mocking API endpoints for testing
```

### No Examples

```markdown
## Authentication
Use OAuth2 to authenticate
```

### With Examples

```markdown
## Authentication

```python
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

client = BackendApplicationClient(client_id=CLIENT_ID)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(
    token_url='https://api.example.com/oauth/token',
    client_secret=CLIENT_SECRET
)
```
```

## Tips

1. **Start simple** - Add details as needed
2. **Real examples** - Use working code
3. **Update regularly** - Skills should remain current
4. **Test with Claude** - Verify that Claude understands
5. **Cross-reference** - Link to related skills
