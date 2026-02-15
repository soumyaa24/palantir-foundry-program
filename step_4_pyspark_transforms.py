"""
Step 4 - Code Repositories: PySpark Transform

Language: Python (PySpark) via Palantir Transforms API
Purpose:  Replicate the visual logic from Contour and Pipeline Builder (Steps 2-3)
          in structured, version-controlled code.

What I did:
- Translated Contour filter logic (dep_delay > 15) into a PySpark filter
- Replicated the join on tail_number from Pipeline Builder
- Added total_delay as a derived column
- Wrote result to a governed output dataset

What I learned:
- The Transforms API abstracts Spark session management
- Using get_json_object for nested fields in arrival_metrics required explicit casting
- Left join preserves flights even when aircraft metadata is missing

Tools used: Palantir Code Repositories, PySpark, Transforms API
"""

from transforms.api import transform, Input, Output
from pyspark.sql import functions as F


@transform(
    output=Output("/Company/Foundry Training/output/delayed_flights_enriched"),
    flights_input=Input("/Company/Foundry Training/raw/flight_data"),
    aircraft_input=Input("/Company/Foundry Training/raw/aircraft_metadata")
)
def compute(flights_input, aircraft_input, output):
    flights_df = flights_input.dataframe()
    aircraft_df = aircraft_input.dataframe()

    # Filter only flights with >15 min delay for initial QA
    delayed = flights_df.filter(F.col("dep_delay") > 15)

    # Join with aircraft metadata to get model info - left join to keep all delayed flights
    enriched = delayed.join(
        aircraft_df,
        delayed["tail_number"] == aircraft_df["tail_number"],
        "left"
    )

    # Add total_delay - combines departure and arrival delay components
    result = enriched.withColumn(
        "total_delay",
        F.col("dep_delay") + F.get_json_object(F.col("arrival_metrics"), "$.arr_delay").cast("double")
    ).select(
        "flight_id",
        "carrier",
        delayed["tail_number"],
        "model",
        "dep_delay",
        "total_delay"
    )

    output.write_dataframe(result)
