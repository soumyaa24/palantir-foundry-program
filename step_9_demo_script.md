# Step 9 - Final Demo

**Presenter**: Soumya Kumari
**Program**: Palantir Foundry Foundations Entry Program
**GitHub**: https://github.com/soumyaa24/palantir-foundry-program

---

## Written Summary

Over the course of this program I built a complete end-to-end data and AI operations system on Palantir Foundry â€” starting from raw airline data and finishing with an AI-assisted operational dashboard.

### Step by Step

**Steps 1-3**: Set up Foundry environment, explored raw flight data in Contour using filters and expressions, built a reproducible pipeline in Pipeline Builder joining flight records with aircraft metadata.

**Step 4**: Translated the visual pipeline into PySpark using Palantir Transforms API. Output dataset: delayed_flights_enriched â€” flights with dep_delay > 15 min, enriched with aircraft model.

**Step 5**: Modeled Flight and Aircraft as Ontology object types, linked via flightOperatedBy relationship on tail_number.

**Step 6**: Built the Flight Delay Operations Center in Workshop â€” filter by carrier, live severity score, Mark as Resolved action button.

**Step 7**: Added Flight Delay Assistant AI agent to the dashboard. It answers operational questions and takes governed write actions after user confirmation.

**Step 8**: Extended the pipeline with Foundry Expectations â€” FAIL on negative delays, WARN on missing tail numbers.

---

## Demo Script (2-3 minutes)

### 0:00 â€“ 0:30 | Pipeline and Lineage

"Hi, I am Soumya Kumari. I will walk you through the flight delay operations tool I built on Palantir Foundry.

I started by exploring raw flight data in Contour, then moved that into a PySpark transform. The output is delayed_flights_enriched â€” filtered for delays over 15 minutes and joined with aircraft metadata."

Show Monocle â€” data lineage from source to output

### 0:30 â€“ 1:15 | Ontology and Functions

"I modeled the data as Ontology objects â€” Flight and Aircraft â€” linked by tail number. This is what allows everything downstream to work with typed objects instead of raw rows.

I also wrote two TypeScript functions: one calculates delay severity in real time, the other lets users bulk-update flight status."

Show Ontology Manager â€” object types, properties, link

### 1:15 â€“ 2:00 | Workshop App

"This is the Flight Delay Operations Center. Users can filter by carrier, see the severity score for selected flights, and mark them as resolved.

I integrated an AIP Logic agent â€” instead of a separate form for every use case, the agent handles operational questions and takes governed actions."

Show Workshop app â€” filter, severity card, AIP Chat

### 2:00 â€“ 2:30 | Data Quality and Wrap-up

"I added Foundry Expectations to the pipeline â€” the build fails on negative delays and warns on missing tail numbers.

The main thing I took from this program is how Foundry connects data engineering, semantic modeling, and AI tooling into one governed environment with full lineage."
