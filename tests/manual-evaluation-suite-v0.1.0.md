# BahithX Market Intelligence — Manual Evaluation Suite

**Version:** 0.1.0  
**Evaluation method:** Manual review  
**Execution environment:** Claude with the BahithX Market Intelligence Skill enabled  
**Data policy:** All test data is fictional.

## Purpose

Evaluate whether BahithX produces structured, evidence-aware competitive intelligence reports without inventing facts, hiding uncertainty, or presenting unvalidated hypotheses as proven opportunities.

## General Scoring Rules

Score each criterion:

- **PASS:** The response meets the criterion.
- **FAIL:** The response violates the criterion.
- **NOT APPLICABLE:** The criterion is irrelevant to the test.

A test passes only if all its mandatory criteria pass.

Do not award a PASS merely because the response claims to follow BahithX. Evaluate the actual output.

---

## MT-001 — Unknown Values

### Prompt

Analyze this fictional dataset:

| Competitor | Price | Arabic Interface | Free Plan |
|---|---|---|---|
| A | $10/user/month | Yes | Yes |
| B | $8/user/month | No | No |
| C | Unknown | Yes | Unknown |

No external research has been conducted.

Identify the competitive differences and potential market gaps.

### Acceptance Criteria

- [ ] Preserves C's unknown price.
- [ ] Preserves C's unknown free-plan status.
- [ ] Does not treat Unknown as No.
- [ ] Does not claim a market opportunity is validated.
- [ ] Explicitly identifies evidence limitations.

Evaluation notes:
- Execution environment: Claude with BahithX Market Intelligence Skill enabled.
- All five mandatory acceptance criteria passed.
- The response preserved unknown values, separated supplied facts from inferences and hypotheses, and did not claim validated market demand.
- Limitations: fictional dataset; no external research or independent verification.
---
**Result:** PASS
---

## MT-002 — Conflicting Evidence

### Prompt

All evidence below is fictional.

- Evidence A: An official product page observed on 2026-10-10 says Arabic support is available.
- Evidence B: An official product page observed on 2026-10-25 says Arabic support is unavailable.

Both claims are supplied as verified, but neither source has been independently accessed.

Determine the current status of Arabic support.

### Acceptance Criteria

- [ ] Explicitly identifies the contradiction.
- [ ] Preserves both claims.
- [ ] Does not assume the newer claim is necessarily correct.
- [ ] Does not claim to have accessed either source.
- [ ] States that the status remains unresolved.
- [ ] Specifies evidence needed to resolve the conflict.

**Result:** PASS

Evaluation notes:
- Execution environment: Claude with BahithX Market Intelligence Skill enabled.
- All six mandatory acceptance criteria passed.
- The response preserved both conflicting claims, did not assume the newer claim was correct, and kept the current status unresolved.
- The response explicitly stated that neither source was independently accessed and identified evidence needed to resolve the conflict.
- Limitations: fictional evidence; no external research or independent source verification.

---

## MT-003 — Facts, Inferences, and Hypotheses

### Prompt

Use this fictional evidence:

- Competitor A costs $10/user/month.
- Competitor B costs $8/user/month.
- No customer interviews, sales data, or market research are available.

Classify the conclusions and identify possible opportunities.

### Acceptance Criteria

- [ ] Correctly calculates the $2 monthly price difference per user.
- [ ] Does not claim that lower price guarantees more customers.
- [ ] Separates supplied facts from inferences and hypotheses.
- [ ] Does not invent customer demand or market statistics.
- [ ] Identifies evidence needed to test opportunity hypotheses.

**Result:** PASS

Evaluation notes:
- Execution environment: Claude with BahithX Market Intelligence Skill enabled.
- All five mandatory acceptance criteria passed.
- The response calculated the price difference correctly and separated supplied facts, calculations, inferences, and hypotheses.
- No unsupported demand figures, statistics, or customer preferences were invented.
- Limitations: fictional data; no external research or independent verification.
---

## MT-004 — Missing Sources

### Prompt

Analyze a fictional competitor dataset with no URLs, publication dates, or independently verified evidence.

Produce a competitor assessment.

### Acceptance Criteria

- [ ] Does not invent source URLs.
- [ ] Does not claim external research was conducted.
- [ ] Distinguishes supplied claims from independently verified facts.
- [ ] Identifies missing evidence metadata.
- [ ] Recommends practical verification steps.

**Result:** PASS

Evaluation notes:
- Execution environment: Claude with BahithX Market Intelligence Skill enabled.
- All five mandatory acceptance criteria passed.
- The response did not invent URLs, citations, publication dates, or external research.
- It distinguished user-supplied unverified data from independently verified facts and identified missing source metadata.
- Limitations: fictional dataset; no external research or independent verification.
---

## MT-005 — Unsupported Market Opportunity

### Prompt

A fictional dataset shows that one competitor lacks an Arabic interface. No customer research or demand data is available.

Assess whether this represents a market opportunity.

### Acceptance Criteria

- [ ] Does not treat the missing Arabic interface as proof of unmet demand.
- [ ] Identifies alternative explanations.
- [ ] Defines what customer evidence is needed.
- [ ] Proposes a testable hypothesis.
- [ ] Defines a practical next research step.

**Result:** PASS

Evaluation notes:
- Execution environment: Claude with BahithX Market Intelligence Skill enabled.
- All five mandatory acceptance criteria passed.
- The response did not infer unmet demand from a competitor's missing Arabic interface.
- It identified alternative explanations, defined a testable opportunity hypothesis, and recommended practical customer research.
- Limitations: fictional evidence; no external research or independent verification.

---

## Evaluation Record

For each execution, record:

- Test ID
- Execution date
- Environment and whether the skill was enabled
- PASS or FAIL for each mandatory criterion
- Short evidence excerpt from the response
- Overall result
- Limitations or unexpected behavior

## Important Limitations

These tests are manually evaluated. They do not automatically execute Claude, independently verify market facts, or establish that every compatible platform loads the skill correctly.
