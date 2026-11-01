# BahithX

An AI skill for evidence-based competitive intelligence, competitor benchmarking, market opportunity analysis, and strategic gap assessment.

## What It Does

BahithX helps structure competitive intelligence by:

- Comparing competitors using supplied evidence.
- Identifying competitive differences and potential strategic gaps.
- Separating supplied facts, inferences, and unvalidated hypotheses.
- Preserving unknown values and flagging conflicting evidence.
- Identifying evidence gaps and recommending practical research steps.
- Producing structured reports with explicit limitations.

## Evidence Standards

BahithX is designed to avoid presenting unsupported claims as established facts.

- Unknown values remain unknown.
- Conflicting claims are identified rather than arbitrarily resolved.
- User-supplied information is distinguished from independently verified evidence.
- Potential opportunities are hypotheses until supported by relevant research.
- Sources are not claimed to have been accessed unless they actually were.

## Repository Structure

- `skills/market-intelligence/SKILL.md` — the market intelligence skill.
- `examples/sample-competitor-data.csv` — fictional sample competitor dataset.
- `tests/test-cases.md` — defined test cases.
- `tests/test-results-v0.1.0.md` — recorded test results.
- `tests/manual-evaluation-suite-v0.1.0.md` — manual behavioral evaluation suite.
- `tests/test_dataset.py` — automated dataset tests.
- `.github/workflows/validate-skill.yml` — automated validation workflow.

## Testing

The repository includes automated validation for the skill and dataset, alongside manual behavioral tests.

Manual evaluation results depend on the tested AI environment and the specific scenarios used. They do not establish real-world market accuracy, commercial viability, or reproducibility across all AI systems.

## Limitations

BahithX structures and analyzes available evidence. It does not independently establish market demand, guarantee the accuracy of supplied data, or prove that a potential market opportunity is commercially viable.

Conclusions depend on the quality, completeness, and reliability of the available evidence.

## Project Status

Version: `0.1.0`

This is an early-stage project. Features, documentation, and evaluation coverage may evolve.

## License

See the [LICENSE](LICENSE) file.
