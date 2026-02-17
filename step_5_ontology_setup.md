# Step 5 - Ontology Setup

The Ontology is the semantic layer between raw data and applications. Instead of querying datasets directly, object types provide a governed, typed, permission-controlled interface.

## What I Did

Modeled two object types â€” Flight and Aircraft â€” and linked them via a relationship backed by the enriched dataset from Step 4.

## Object Types

### Flight

| Property | Type | Source Column |
|----------|------|---------------|
| flightId | String | flight_id |
| carrier | String | carrier |
| tailNumber | String | tail_number |
| depDelay | Double | dep_delay |
| totalDelay | Double | total_delay |

- Primary Key: flightId
- Source: /Company/Foundry Training/output/delayed_flights_enriched

### Aircraft

| Property | Type | Source Column |
|----------|------|---------------|
| tailNumber | String | tail_number |
| model | String | model |

- Primary Key: tailNumber
- Source: /Company/Foundry Training/raw/aircraft_metadata

## Relationship: Flight to Aircraft

```
Flight (many)
    |
    | flightOperatedBy
    | via: Flight.tailNumber = Aircraft.tailNumber
    v
Aircraft (one)
```

- Link Name: flightOperatedBy
- Cardinality: Many-to-one

Steps in Ontology Manager:
1. Open Ontology Manager > Links tab > + New Link
2. Set From: Flight.tailNumber, To: Aircraft.tailNumber
3. Name: flightOperatedBy, Cardinality: Many to One
4. Click Publish

## Why Ontology Matters

Without the ontology layer, Workshop cannot display live typed objects, TypeScript Functions cannot accept Flight[] as a parameter, and AIP Logic has no structured objects to reason about. The ontology makes everything downstream governed and typed.

## What I Learned

- Object types carry permissions and audit trails â€” not just data wrappers
- The Flight-Aircraft relationship mirrors a foreign key but enables navigation in Workshop
- Getting the primary key right matters â€” if flightId is not unique, object sync duplicates
- I initially set up the link direction wrong (Aircraft to Flight instead of Flight to Aircraft) and had to recreate it

## Syncing

1. Click Sync Objects â€” populates objects from source datasets
2. Click Publish Ontology â€” makes objects available to Workshop and Functions
