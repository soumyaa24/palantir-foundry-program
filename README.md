# Palantir Foundry Foundations Entry Program

**Soumya Kumari** | [@soumyaa24](https://github.com/soumyaa24)

---

## Project: Flight Delay Operations Center

I built an end-to-end flight delay monitoring and operations tool on Palantir Foundry. The goal was to take raw airline data and build something an operations team could actually act on â€” not just a read-only dashboard.

Getting everything to connect across pipeline to ontology to workshop to AI took more back-and-forth than I expected, but that is mostly what this program is about.

## What I Built

- A PySpark transform that filters delayed flights (>15 min) and joins them with aircraft metadata
- An Ontology with Flight and Aircraft object types linked by tail number
- TypeScript Functions for real-time delay severity scoring and bulk status updates
- A Workshop app â€” Flight Delay Operations Center â€” where users filter, assess, and resolve flights
- An AIP Logic agent embedded in the app for natural language queries and governed write actions
- Data Expectations on the pipeline to catch bad data before it reaches the Ontology

## Repository Structure

| Step | File | What it covers |
|------|------|----------------|
| 0-3 | steps_1_2_3_platform_guide.md | Enrollment, Contour exploration, Pipeline Builder |
| 4 | step_4_pyspark_transforms.py | PySpark transform â€” filter, join, enrich |
| 5 | step_5_ontology_setup.md | Object types, properties, Flight to Aircraft link |
| 6 | step_6_workshop_app.md | Workshop layout, widgets, action button |
| 6/8 | step_6_8_logic_extension.ts | TypeScript functions â€” severity scoring and bulk update |
| 7 | step_7_aip_logic.md | AIP Logic agent â€” tools, system prompt, testing |
| 8 | step_8_health_checks.py | Foundry Expectations â€” data quality gates |
| 9 | step_9_demo_script.md | Demo script and written project summary |

## Pipeline Output Sample

What the enriched dataset looks like after Step 4 runs:

```
flight_id | carrier | tail_number | model         | dep_delay | total_delay
AA1023    | AA      | N12345      | Boeing 737    | 87.0      | 112.0
UA4412    | UA      | N67890      | Airbus A320   | 35.0      | 48.0
DL7701    | DL      | N11223      | Boeing 757    | 22.0      | 31.0
WN5533    | WN      | N44556      | Boeing 737    | 63.0      | 79.0
```

Severity from getDelaySeverity:
- AA1023 = CRITICAL (avg dep_delay > 60)
- UA4412 = WARNING (avg dep_delay 30-60)
- DL7701 = NORMAL (avg dep_delay < 30)

## Challenges and Learnings

**Step 4 (PySpark)**: The join itself was fine but get_json_object on the nested arrival_metrics field kept returning null. Had to add an explicit Double cast. Took about an hour to figure out.

**Step 5 (Ontology)**: Set up the link direction wrong initially â€” Aircraft to Flight instead of Flight to Aircraft. The Workshop table showed an empty relation. Had to delete and recreate the link.

**Step 7 (AIP Logic)**: System prompt took three rewrites. First version triggered write actions without asking for confirmation. Explicitly added "always confirm before write actions" to fix it.

**Step 8 (Expectations)**: Did not realize a FAIL expectation stops the entire pipeline build. Set the tail_number check to FAIL first, which blocked my own pipeline. Switched to WARN after.

## Stack

Python Â· PySpark Â· TypeScript Â· Palantir Transforms API Â· Ontology Manager Â· Workshop Â· AIP Logic Â· Foundry Expectations

---

*Palantir Foundry Foundations Entry Program â€” Soumya Kumari, 2026*
