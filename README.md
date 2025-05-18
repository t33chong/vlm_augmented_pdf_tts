## Using a vision-language model to augment technical PDFs for synthesized speech intelligibility and accessibility

### Impetus and approach

I learn best via audio, but the textbooks and research papers I'm interested in tend to convey a substantial amount of information through charts and diagrams. All of the text-to-speech reader apps I've tried so far omit this content. They're also pretty terrible at pronouncing mathematical expressions and narrating code while preserving its logical flow. Perhaps most egregiously, the way they read tables out loud from left to right and top to bottom as garbled streams of numbers not only fails to communicate the authors' intent; it makes my brain tune out.

My first attempts at preprocessing textbooks with LLMs before feeding them through TTS leveraged `gpt-4o`, which at the time of writing is just under 53 weeks old. I managed to get decent results, but it required a lot of arm-twisting and manual work, e.g.:
1. First, get it to preface chapter/section titles with octothorpes (to mark them for inclusion in the table of contents) and rewrite abbreviations as they should be pronounced.
2. On the second pass, get it to focus on articulating mathematical expressions correctly (not always reliable - at one point I considered enabling function calling with a deterministic tool based on [speech-rule-engine](https://mathjax.github.io/MathJax-demos-web/speech-generator/convert-with-speech.html)).
3. On the third pass, get it to narrate figures/tables in a way that gets the intended point across.
4. Ditto for code snippets, and so on...

It couldn't walk and chew gum at the same time; tweaking the prompt to fix one thing would break another. Then, because context length limitations (both direct and indirect since [instruction-following ability degrades as token count increases](https://arxiv.org/abs/2402.14848v1)) made it necessary to break chapters into multiple PDF files: write a separate script that uses rule-based heuristics to join paragraphs that start on one page and end on the next.

I had already started working on an agentic system that would orchestrate these tasks when the combination of Gemini 2.5 Pro's stellar [vision metrics](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard) and order of magnitude improvement in long context relative to 4o compelled me to try simple prompting again. Given a 20-page PDF (Chapter 9 of Jurafsky and Martin's [Speech and Language Processing 3E](https://web.stanford.edu/~jurafsky/slp3/) draft), Gemini got it all done in one shot.

The code here is pretty simple, mostly lifted directly from Google's [AI Studio](https://aistudio.google.com) and [Gen AI SDK](https://github.com/googleapis/python-genai) docs but with a bit of added concurrency since prompts and outputs containing full chapters + the model's initial Chain-of-Thought reasoning, and the transformer architecture's quadratic runtime, can push generation time (latency per request) above 4 minutes. Most of my effort went into the prompt, which certainly has room for improvement; for example, sometimes the model ignores my directions to exempt section titles from phonemic annotation.

Regarding the TTS itself, I attempted to swap out Edge for [`kokoro`](https://github.com/hexgrad/kokoro) in [`epub2tts-edge`](https://github.com/aedocw/epub2tts-edge) which accepts plain text files in this format but ran into some issues with `ffmpeg` timestamp metadata during the concatenation phase. I wanted the audiobook done before flying cross-country for commencement at UPenn, so I wrote a hacky script to compile a barebones .epub file that I could pass into a local fork of [`audiblez`](https://github.com/santinic/audiblez) that I've modified to parallelize TTS generation across multiple Nvidia GPUs (upstreaming this is on my to-do list).

### Usage

```bash
python3 -m venv .venv  # or uv venv --python=3.12
. .venv/bin/activate
pip3 install -r requirements.txt  # or uv pip install -r requirements.txt
cp .env.example .env
```

Then, obtain a Gemini API key and edit `.env` accordingly. Finally:

```bash
python3 process_pdfs.py 1.pdf 2.pdf  # ... N.pdf
```

The resulting text files might require concatenation.

### Disclaimers

- The visual impairment motive referenced in the prompt is a fib - to an extent anyway, lenses serve me well - intended to crystallize intent.
- The given phonemic inventory is pseudo-IPA (used in Kokoro's underlying [grapheme-to-phoneme conversion](https://github.com/hexgrad/misaki/blob/main/EN_PHONES.md)).
- I would usually use [OpenAI's Python SDK](https://github.com/openai/openai-python) and [LiteLLM proxy server](https://github.com/BerriAI/litellm?tab=readme-ov-file#litellm-proxy-server-llm-gateway---docs) to facilitate experimentation with different API providers and models, but:
  - For aforementioned reasons, I had Gemini 2.5 Pro in mind specifically for this project
  - Google's native API has better support for PDFs (last I checked, OpenAI's SDK required conversion to JPEG/PNG, which re-encodes the original PDF's text content less efficiently/more lossily and introduces a layer of indirection [OCR or ViT])
- I have withheld output lest I violate copyright law.
