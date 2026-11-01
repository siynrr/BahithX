# BahithX Market Intelligence Skill — Test Cases

**Version:** 0.1.0  
**Status:** Initial test specification  
**Dataset:** Fictional competitor data  
**Purpose:** Evaluate analytical accuracy, evidence handling, and the quality of market opportunity hypotheses.

---

## 1. Test Objectives

These tests evaluate whether BahithX:

1. Preserves the information provided in the dataset.
2. Compares competitors accurately.
3. Distinguishes unknown information from negative findings.
4. Separates recorded facts from analytical inferences and assumptions.
5. Generates testable opportunity hypotheses without inventing market demand.
6. Identifies limitations in the available evidence.
7. Recommends appropriate validation steps.

Passing these tests does not establish that a real market opportunity exists.

## 2. Test Dataset

The baseline dataset contains three fictional competitors:

- Northstar
- TaskPilot
- FlowDesk

Each competitor has four recorded attributes:

- Free Plan
- Arabic Support
- Monthly Price
- API Integration

The dataset contains 12 records.

### Expected Baseline Values

| Attribute | Northstar | TaskPilot | FlowDesk |
|---|---|---|---|
| Free Plan | Yes | No | Yes |
| Arabic Support | Unknown | Yes | No |
| Monthly Price | $12 per user | $9 per user | Unknown |
| API Integration | Yes | Unknown | Yes |

These values are fictional and are used exclusively for testing.

## 3. Test Cases

### TC-001: Dataset Integrity

**Objective:** Verify that all supplied values are preserved.

**Input:** The complete baseline CSV dataset.

**Expected results:**

- All three competitors are included.
- All four attributes are compared.
- No recorded value is changed.
- No competitor or feature is invented.
- The report identifies the dataset as fictional.

**Pass criteria:** Every value in the comparison matches the original dataset.

### TC-002: Unknown Information Handling

**Objective:** Verify that missing information is not interpreted as a missing capability.

**Input:** The baseline dataset.

**Expected results:**

- Northstar's Arabic support is classified as unknown.
- TaskPilot's API integration status is classified as unknown.
- FlowDesk's monthly price is classified as unknown.
- No conclusion is drawn that these competitors lack the unknown capabilities.

**Pass criteria:** Every unknown value remains explicitly unknown, and no unsupported negative claim is made.

### TC-003: Price Comparison Accuracy

**Objective:** Verify that price comparisons are mathematically correct.

**Input:**

- Northstar: $12 per user per month.
- TaskPilot: $9 per user per month.
- FlowDesk: Unknown.

**Expected results:**

- TaskPilot's recorded price is $3 lower per user per month than Northstar's.
- TaskPilot's price is 25% lower than Northstar's recorded price.
- FlowDesk is excluded from numerical price ranking because its price is unknown.
- The report notes that equivalent plan features and pricing conditions have not been established.

**Pass criteria:** Calculations are correct, and no unsupported price comparison is made.

### TC-004: Fact, Inference, and Assumption Separation

**Objective:** Verify that conclusions are classified appropriately.

**Expected results:**

**Recorded facts:**
- Two competitors are listed as offering a free plan.
- One competitor is listed as supporting Arabic.
- Two competitors are listed as supporting API integration.

**Analytical inferences:**
- Arabic support differs across the recorded competitors.
- Free-plan availability differs across the recorded competitors.

**Assumptions requiring validation:**
- Some Arabic-speaking customers may need a different product experience.
- Some customers may prefer a particular free-plan structure.
- Some companies may need API integrations that their current tools do not provide.

**Pass criteria:** The report does not present assumptions as verified customer needs or established commercial opportunities.

### TC-005: Opportunity Hypothesis Quality

**Objective:** Verify that proposed opportunities are testable.

**Expected results:**

The report proposes three hypotheses related to:

1. Arabic-language product experience.
2. Free-plan design and pricing.
3. API integration requirements.

Each hypothesis includes:

- A clearly defined research question.
- The evidence currently available.
- The additional evidence required.
- A practical validation experiment.
- A decision criterion.

**Pass criteria:** Each hypothesis includes a test that could produce evidence for or against it.

The report explicitly states that the fictional dataset does not establish real customer demand.

### TC-006: Evidence Integrity

**Objective:** Prevent fabricated sources and unsupported claims.

**Expected results:**

- No fabricated URLs, citations, statistics, customer interviews, or market research findings.
- No claim that external research was conducted unless it actually occurred.
- The fictional status of the dataset is disclosed.
- Missing evidence is explicitly identified.

**Pass criteria:** Every factual claim about the dataset is traceable to its supplied records, and external claims are supported by sources actually consulted.

### TC-007: Conflicting Evidence

**Objective:** Verify that contradictory information is not silently reconciled.

**Test fixture:** Create a separate test copy in which two purported sources disagree about whether Northstar supports Arabic.

**Expected results:**

- The disagreement is explicitly identified.
- The sources and their reliability are assessed if source details are provided.
- The capability is not classified as definitively present or absent without adequate resolution.
- Additional verification steps are recommended.

**Pass criteria:** The report preserves the uncertainty and explains what evidence would resolve it.

**Note:** This is a separate synthetic test fixture. Do not modify the baseline CSV to run it.

### TC-008: Recommendations and Limitations

**Objective:** Verify that recommendations reflect the available evidence.

**Expected results:**

- The report distinguishes competitive differences from validated market gaps.
- It identifies customer research as necessary to establish demand.
- It does not invent market size, revenue forecasts, or probabilities of success.
- It recommends practical next steps appropriate to the evidence.

**Pass criteria:** No commercial opportunity is presented as proven solely from the baseline dataset.

---

## 4. Test Execution Record

Record the results of each test after executing the skill.

| Test ID | Result | Evidence or Notes |
|---|---|---|
| TC-001 | Not run | |
| TC-002 | Not run | |
| TC-003 | Not run | |
| TC-004 | Not run | |
| TC-005 | Not run | |
| TC-006 | Not run | |
| TC-007 | Not run | |
| TC-008 | Not run | |

Use the following result labels:

- **PASS:** All stated pass criteria are satisfied.
- **FAIL:** One or more pass criteria are violated.
- **BLOCKED:** The test cannot be evaluated because required input or functionality is unavailable.
- **NOT RUN:** The test has not been executed.

Do not mark a test as passed merely because the output appears professional.

## 5. Acceptance Criteria

The initial skill version is ready for further development when:

- All eight tests have been executed.
- All critical data-integrity and evidence-handling tests pass.
- Any failures have been documented and addressed.
- The final report remains consistent with the supplied data.
- Known limitations are documented.

These criteria evaluate the initial analytical workflow. They do not establish market validity, universal model compatibility, or commercial readiness.

## 6. Scope Limitations

This specification describes analytical acceptance tests, not automated software tests.

The tests require a compatible AI environment, the skill instructions, the dataset, and human review of the generated report.

Automated validation may be introduced in a later version.
