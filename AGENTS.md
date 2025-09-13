# Repository Guidelines

## Project Structure & Module Organization
- Root scripts: `download_google_images.py`, `listar_vozes.py`, `fala.py`, `gwps.py`.
- Assets: `imagens/` (downloaded images) and `index.html` demo page.
- Learning notes: `apredizado/` (docs and examples).
- Vendored tools: `blender-4.5.1-linux-x64/` (do not edit or commit changes here).
- Dependency pins: `requirements.txt`. Generated artifacts like `vozes.txt` should not be versioned.

## Build, Test, and Development Commands
- Create a virtual env: `python3 -m venv .venv && source .venv/bin/activate`.
- Install deps: `pip install -r requirements.txt` (add `playsound` if using `fala.py`).
- Run image fetcher: `python download_google_images.py "boeing 737" -c 10 -f imagens/boeing_737`.
- List ElevenLabs voices: `ELEVEN_API_KEY=... python listar_vozes.py`.
- Text-to-speech: `ELEVEN_API_KEY=... python fala.py -v Jessica "Olá, mundo"`.

## Coding Style & Naming Conventions
- Python 3.10+, 4‑space indentation, PEP 8; prefer type hints on public functions.
- Use `snake_case` for files and functions; avoid spaces in new filenames.
- Keep scripts CLI-friendly using `if __name__ == "__main__":` and `argparse`.
- When adding dependencies, update `requirements.txt` and include a usage note in the file header.

## Testing Guidelines
- No test framework is enforced yet. Provide minimal smoke tests or example invocations in docstrings/README notes.
- For logic-heavy additions, add self-contained functions and test them with small fixtures under a `tests/` folder (pytest or unittest acceptable).
- Ensure commands fail fast with clear error messages and exit codes.

## Commit & Pull Request Guidelines
- Commits: imperative, present tense (e.g., "Add CLI for image fetch"); group related changes; reference issues with `#id`.
- PRs must include: purpose, short summary of changes, reproduction/usage examples (commands), and screenshots when UI is affected.
- Do not mix refactors with feature changes; keep diffs focused.

## Security & Configuration
- Never commit secrets. Use `ELEVEN_API_KEY` via environment variables (or a local `.env` ignored by Git).
- Treat large binaries as external assets; avoid modifying `blender-4.5.1-linux-x64/`. Use Git LFS if adding media.
- Validate and sanitize all downloaded content; delete invalid files after checks (as in the image script).
