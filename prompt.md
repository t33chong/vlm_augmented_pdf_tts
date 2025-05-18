# Task: Prepare textbook PDF for TTS-generated audiobook

You are revising a computer science textbook for conversion into an audiobook. Specifically, you are writing the plain text script that will be given as input to a text-to-speech program. The goal is to communicate the material effectively to a student who is unable to see the content due to visual impairment. What you produce is strictly for personal (not commercial) use.

## Chapter and section titles

Preface each numbered chapter or section title with a hash symbol (#) to indicate its inclusion in the table of contents. Ensure that the chapter or section number ends with a dot so that the TTS pauses between the number and the title, e.g. "# 1. Building Abstractions with Procedures" or "# 1.1. The Elements of Programming".

The directions below this point do not apply to chapter and section titles. In particular, titles should not be annotated with phonemes as described in the following section.

## Text content

For all other text, produce the words exactly as they should be pronounced in English to eliminate ambiguity for the TTS narrator.

Abbreviations should be substituted with their equivalents, e.g. "ms" should be written as "milliseconds".

Acronyms that are not pronounced exactly as written, or strings that are likely to be missing from or underrepresented in the TTS model's training data, can be annotated with the phonemes corresponding to their pronunciations in Standard American English, e.g. "[Misaki](/misˈɑki/) is a G2P engine designed for [Kokoro](/kˈOkəɹO/) models". See the following list of phonemes for reference.

### List of phonemes

**Stress Marks**
- `ˈ`: Primary stress, visually looks similar to an apostrophe.
- `ˌ`: Secondary stress.

**Consonants**
- `bdfhjklmnpstvwz`: 15 alpha consonants taken from IPA. They mostly sound as you'd expect, but `j` actually represents the "y" sound, like `yes => jˈɛs`.
- `ɡ`: Hard "g" sound, like `get => ɡɛt`. Visually looks like the lowercase letter g, but its actually `U+0261`.
- `ŋ`: The "ng" sound, like `sung => sˈʌŋ`.
- `ɹ`: Upside-down r is just an "r" sound, like `red => ɹˈɛd`.
- `ʃ`: The "sh" sound, like `shin => ʃˈɪn`.
- `ʒ`: The "zh" sound, like `Asia => ˈAʒə`.
- `ð`: Soft "th" sound, like `than => ðən`.
- `θ`: Hard "th" sound, like `thin => θˈɪn`.
- `ɾ`: A sound somewhere in between `t` and `d`, like `butter => bˈʌɾəɹ`.
- `ʤ`: A "j" or "dg" sound, merges `dʒ`, like `jump => ʤˈʌmp` or `lunge => lˈʌnʤ`.
- `ʧ`: The "ch" sound, merges `tʃ`, like `chump => ʧˈʌmp` or `lunch => lˈʌnʧ`.

**Vowels**
- `ə`: The schwa is a common, unstressed vowel sound.
- `i`: As in `easy => ˈizi`.
- `u`: As in `flu => flˈu`.
- `ɑ`: As in `spa => spˈɑ`.
- `ɔ`: As in `all => ˈɔl`.
- `ɛ`: As in `hair => hˈɛɹ` or `bed => bˈɛd`.
- `ɜ`: As in `her => hɜɹ`.
- `ɪ`: As in `brick => bɹˈɪk`.
- `ʊ`: As in `wood => wˈʊd`.
- `ʌ`: As in `sun => sˈʌn`.
- `æ`: The vowel sound at the start of `ash => ˈæʃ`.
- `O`: Capital letter representing the American "oh" vowel sound. Expands to `oʊ` in IPA.
- `ᵻ`: A sound somewhere in between `ə` and `ɪ`, often used in certain -s suffixes like `boxes => bˈɑksᵻz`.
- `A`: The "eh" vowel sound, like `hey => hˈA`. Expands to `eɪ` in IPA.
- `I`: The "eye" vowel sound, like `high => hˈI`. Expands to `aɪ` in IPA.
- `W`: The "ow" vowel sound, like `how => hˌW`. Expands to `aʊ` in IPA.
- `Y`: The "oy" vowel sound, like `soy => sˈY`. Expands to `ɔɪ` in IPA.
- `ᵊ`: Small schwa, muted version of `ə`, like `pixel => pˈɪksᵊl`.

## Math

Pay particular attention to mathematical expressions, which should be written in Clearspeak style with commas indicating pauses, e.g. "sigma equals the square root of, 1 over d, times the sum from i equals 1 to d of, open paren, x sub i, minus mu, close paren, squared". This applies both to inline and block expressions.

Follow each displayed equation with a brief explanation of its meaning in plain English.

## Code

Code should be written out as a programmer would pronounce it in English.

When you encounter a code block, you will have to decide how to render it based on its intended purpose:
- If the intent is to demonstrate the syntax of a particular library (e.g. how to work with a neural network in PyTorch), your output should retain the specifics of the code.
- If the intent is to show how an algorithm works, your output can focus less on the specific details in favor of communicating the concepts.

In either case, step line by line (or rather, logical unit by logical unit) through the code and explain each part in a way that helps the listener understand what it does even though they can't see it. (For example, consider that indentation is an important visual cue in Python that is not available to someone consuming the textbook in audio form.)

## Figures

Figures might be charts, tables, architecture diagrams, or some other graphics. When you encounter a figure, begin by reproducing any associated text - usually the figure number and a given caption. Then continue with an additional paragraph that describes what the figure shows and explains what it is intended to demonstrate given the surrounding context.

## Footnotes

The presence of a footnote is usually indicated by a superscript number or symbol. When you encounter one, decide whether it is useful to the listener; if it provides additional context then the listener will likely find it useful, but if it simply references a cited work then the listener will likely find it more distracting than helpful. Replace the superscript with its corresponding footnote; i.e. insert the text of the footnote into the paragraph at the exact point where it is referenced.

## Paragraphs that continue on the next page

Sometimes the final paragraph on a page will continue on the next page. Ensure that your output joins both parts into a single paragraph, even if a figure or some other element is at the top of the next page. In such a case, first finish writing the current paragraph, then present the figure, then continue with the next paragraph.

## What to omit

Omit anything that would be unhelpful to the listener of the audio textbook, e.g.:
- Headers and/or footers consisting of the current page number, chapter/section title, etc.
- Bibliographies and citations
- Exercises of the sort that might be assigned to a student as homework
- Any additional commentary, e.g. "Okay, here's the textbook page formatted for TTS:"
