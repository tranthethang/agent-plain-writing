# Limitations

- **The checker is mechanical.** It does not judge voice.
- **The numeric limits are starting estimates.** Nobody has verified them as standards. Run the checker on real texts from your team and adjust `profile.json`.
- **Japanese has no native review.** An AI improved the `ja` content. Register (です・ます調, だ・である調, or である調 / 常体 by type), requirement words and example pairs need review by a native speaker before real use.
- **Examples are illustrations.** Stories and numbers in `examples/` are not real facts. In real work, use the author's facts or write `TBD`.
- **No proof of effect yet.** See [05-evals](05-evals.en.md). The only evidence is one run, see [evidence/](../../evidence/README.md).
- **Few automated tests.** Tests cover only the `TBD-n` statistics in `evals/score.py` (`python3 -m unittest discover -s tests`). `AGENTS.md` lists the manual checks for the rest.
- **Out-of-scope types.** `prose`, `poetry`, and `screen-design` are out of scope for now.

## Contributing

Read `AGENTS.md` first. It keeps the three language folders parallel and says which file owns which fact.

## License

GNU GPL v3. See `LICENSE`.
