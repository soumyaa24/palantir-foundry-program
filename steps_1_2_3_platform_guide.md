# Steps 0, 1, 2 & 3 â€” Getting Started on Foundry

## Step 0: Enrollment & Progress Tracking

I have successfully submitted the enrollment form and started weekly tracking.

- Enrolled in the Palantir Foundry Foundations Entry Program via Analyticore
- Committed to submitting weekly progress updates via the provided Google Form
- Set a personal goal to complete all 9 steps within the program timeline

---

## Step 1: Environment Setup

I signed up for a developer trial at palantir.com/aip/developers. The account was activated within 24 hours.

### My Completion Evidence

- **Account Activation**: Developer environment activated within 24 hours of registration
- **Workspace**: `Foundry Training - Flight Operations`
- **Tools confirmed accessible**: Contour, Pipeline Builder, Code Repositories, Ontology Manager, Workshop, AIP Logic
- **Verification**: Logged in, confirmed environment was active, and proceeded directly to Step 2

---

## Step 2: Data Exploration in Contour

Contour is a visual query builder â€” essentially a no-code SQL interface where you chain boards together.

### What I Did
1. Imported raw flight data as a Table Board
2. Added a Filter Board â€” kept only rows where dep_delay > 0
3. Created a new column using an Expression Board â€” dep_delay + arr_delay as total_delay
4. Summarized with a Pivot Table Board â€” total delay grouped by carrier
5. Saved the result as a dataset for downstream use in Step 4

### What I Learned
- Contour uses a visual transformation flow â€” each board is a discrete operation
- Filters and aggregations work like SQL WHERE and GROUP BY
- Expression boards can reference any upstream column
- The output dataset from Contour feeds directly into pipelines and code repos
- The same output produced visually here was later reproduced in PySpark (Step 4)

**What was hard**: Expression Boards handle nulls differently than I expected â€” had to add explicit null checks.

---

## Step 3: Building a Pipeline in Pipeline Builder

### What I Did
1. Added two input datasets:
   - Input 1: /Company/Foundry Training/raw/flight_data
   - Input 2: /Company/Foundry Training/raw/aircraft_metadata
2. Connected them with a Join transform on tail_number
3. Added a Filter step â€” dep_delay > 15
4. Output: /Company/Foundry Training/output/delayed_flights_enriched
5. Set materialization to scheduled (daily at 6AM)

### Dataset Summary

| Role | Path |
|------|------|
| Input | /Company/Foundry Training/raw/flight_data |
| Input | /Company/Foundry Training/raw/aircraft_metadata |
| Output | /Company/Foundry Training/output/delayed_flights_enriched |

**Materialization**: Scheduled daily. Manual runs available via the Build button.

### What I Learned
- Pipeline Builder is for production â€” Contour is the scratchpad, this is the factory
- Materialization controls when Foundry runs the pipeline and writes output

---

## Notes

- Steps 0-3 are done entirely in the Foundry UI â€” no local code required
- The logic from Steps 2 and 3 is replicated in PySpark in Step 4
