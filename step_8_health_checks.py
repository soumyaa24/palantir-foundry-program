"""
Step 8 - Exploration: Data Quality Checks with Foundry Expectations

What I explored:
Added data validation checks to the enriched flights pipeline to ensure null values
and negative delays do not silently corrupt the Workshop application logic.

The problem I was solving:
During testing, the Workshop severity card behaved unexpectedly when some flights had
NULL total_delay values. The severity function averaged them as 0, hiding real delays.
Adding quality gates at the pipeline level catches this before data reaches the Ontology.

What I added:
1. FAIL condition - any row with dep_delay < 0 fails the build entirely.
   Negative delays are physically impossible and indicate an upstream ingestion error.

2. WARN condition - rows with NULL tail_number trigger a warning.
   These flights cannot be linked to an Aircraft object, breaking the Ontology relationship.

Lesson learned:
FAIL stops the entire pipeline build. I initially set the tail_number check to FAIL,
which blocked my own pipeline on the first run. Switched it to WARN after that.

Tools used: Palantir Transforms API, Foundry Expectations
"""

from transforms.api import transform, Input, Output
from transforms.expectations import Expectations, Expectation


@transform(
    output=Output("/Company/Foundry Training/output/validated_flights"),
    input_df=Input("/Company/Foundry Training/output/delayed_flights_enriched")
)
@Expectations(
    Expectation(
        "no_negative_delays",
        "dep_delay >= 0",
        action="FAIL"
    ),
    Expectation(
        "valid_tail_numbers",
        "tail_number IS NOT NULL",
        action="WARN"
    )
)
def compute(input_df, output):
    output.write_dataframe(input_df.dataframe())
