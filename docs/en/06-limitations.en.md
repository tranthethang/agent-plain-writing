# Limitations

- **The checker is mechanical.** It does not judge voice.
- **The numeric limits are starting estimates.** Nobody has verified them as standards. Run the checker on real texts from your team and adjust `profile.json`.
- **Examples are illustrations.** Stories and numbers in `examples/` are not real facts. In real work, use the author's facts or write `TBD-n`.
- **No proof of effect yet.** See [05-evals](05-evals.en.md). The evidence is one run per version, see [evidence/](../../evidence/README.md).
- **Few automated tests.** Tests cover the `TBD-n` statistics in `evals/score.py`, the document-type set, the checker default type, the checker's table-cell, report-label and `--short-brief` checks, the Units tables, the shipped samples in `examples/`, the report marker in `evals/score.py` (`strip_trailing_report`), the time and date token count, the `PLAIN-WRITING.md` search from a subfolder, the length warning above the upper limit only, the `doc-types/` file for every type, and the `--judge-prompts` option and the with-skill prompt of `evals/run_eval.py` (`python3 -m unittest discover -s tests`). `AGENTS.md` lists the manual checks for the rest.
- **Out-of-scope types.** `prose`, `poetry`, and `screen-design` are out of scope for now.

## Contributing

Read `AGENTS.md` first. It keeps the three language folders parallel and says which file owns which fact.

## License

GNU GPL v3. See `LICENSE`.
