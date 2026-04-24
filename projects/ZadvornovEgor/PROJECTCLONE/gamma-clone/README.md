# SlideDeck AI -- AI Presentation Generator

MVP clone of [Gamma.app](https://gamma.app): describe a topic, get a styled slide deck.

## Architecture

```
User Input (topic, slides, theme)
        |
        v
  +-------------+     +-------------+     +--------------+
  | prompts.py  | --> | slide_gen.  | --> | pptx_builder |
  | (prompt eng)|     | (Claude API)|     | (.pptx file) |
  +-------------+     +-------------+     +--------------+
                            |
                            v
                     +-------------+     +-------------+
                     | preview.py  |     | templates.py|
                     | (HTML cards)|     | (3 themes)  |
                     +-------------+     +-------------+
                            |
                            v
                      +-----------+
                      |  app.py   |
                      | (Streamlit)|
                      +-----------+
```

## Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| UI           | Streamlit          |
| LLM          | Claude (Anthropic) |
| Data models  | Pydantic v2        |
| PPTX export  | python-pptx        |
| Config       | python-dotenv      |

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env with your API key
cp .env.example .env
# Edit .env and paste your ANTHROPIC_API_KEY

# 3. Run the app
streamlit run app.py
```

## File Overview

| File              | LOC  | Purpose                                |
|-------------------|------|----------------------------------------|
| config.py         | ~20  | Env vars, defaults                     |
| models.py         | ~45  | Pydantic schemas                       |
| prompts.py        | ~95  | Prompt engineering (documented)        |
| slide_generator.py| ~115 | Claude API orchestration + retry       |
| pptx_builder.py   | ~170 | .pptx file construction                |
| preview.py        | ~80  | HTML/CSS slide preview                 |
| templates.py      | ~55  | Theme presets                          |
| app.py            | ~130 | Streamlit UI                           |

## License

MIT
