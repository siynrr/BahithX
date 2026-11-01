# BahithX — Market Intelligence Skill

BahithX is an open-source Agent Skill for structured competitive intelligence, competitor benchmarking, strategic gap analysis, and market opportunity assessment.

## Capabilities

- Compare competitor features and pricing using supplied evidence.
- Distinguish facts, inferences, assumptions, and unknowns.
- Identify conflicting evidence without arbitrarily selecting a claim.
- Develop testable market opportunity hypotheses.
- Produce structured reports with explicit limitations.

## Installation

1. Download or clone the BahithX repository.
2. Locate `skills/market-intelligence/`.
3. Install or register that directory using the skill-loading mechanism supported by your compatible AI agent.
4. Ask the agent to use the Market Intelligence Skill for a competitive analysis.

Installation procedures vary by AI agent. Placing the files in a GitHub repository alone does not automatically install the skill into an AI application.

## Validation

The repository includes a GitHub Actions workflow that validates the skill's structure and metadata.

See `../../tests/test-cases.md` for the test cases and `../../tests/test-results-v0.1.0.md` for the current manual evaluation results.

## Limitations

BahithX is an instruction-based skill. Its output depends on the AI agent, available tools, supplied evidence, and execution environment.

A successful structural validation does not establish analytical accuracy or prove that the skill has been loaded and executed by an AI agent.

Market opportunity hypotheses require independent validation before being treated as business conclusions.
