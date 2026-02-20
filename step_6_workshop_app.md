# Step 6 - Workshop Application

**App Name**: Flight Delay Operations Center

An operational dashboard for monitoring and acting on delayed flights. Powered by Flight Ontology objects from Step 5 and TypeScript Functions from Step 6/8.

## What I Did

Built a Workshop app where users can:
- Filter delayed flights by carrier
- See a live severity score (NORMAL / WARNING / CRITICAL) for selected flights
- Mark selected flights as resolved via an action button
- Chat with an embedded AIP Logic agent (added in Step 7)

The entire app is backed by Flight Ontology objects â€” not raw dataset rows.

## Creating the App

1. Open Workshop from Foundry sidebar
2. Click + New Application
3. Name: Flight Delay Operations Center
4. Click Create

## Widgets

### Object Table
1. Drag an Object Table widget onto the canvas
2. Set Object Type to Flight
3. Columns: flightId, carrier, tailNumber, depDelay, totalDelay

### Severity KPI Card
1. Add a Variable widget â€” type: Function â€” choose FlightActions.getDelaySeverity
2. Bind input to Object Table selected rows
3. Display output in a Text widget
4. Conditional colors: CRITICAL = red, WARNING = orange, NORMAL = green

### Filter Bar
1. Add a Filter widget at the top
2. Bind to Object Table, filter by carrier

## Action Button

1. Add a Button widget â€” label: Mark as Resolved
2. On Click > Call Function > FlightActions.bulkUpdateStatus
3. Bind flights to Object Table selected rows
4. Set newStatus to "RESOLVED"

## Layout

```
+--------------------------------------------------+
|  Filter: [ Carrier ]          [Mark as Resolved] |
|                                                  |
|  Severity: [ CRITICAL ]                          |
|                                                  |
|  flightId | carrier | depDelay | totalDelay      |
|  AA1023   | AA      | 87 min   | 112 min         |
|  UA4412   | UA      | 35 min   | 48 min          |
+--------------------------------------------------+
```

## What I Learned

- Workshop widgets bound to Ontology objects update live â€” no page reload needed
- I had to handle the empty selection state explicitly â€” getDelaySeverity returns "Select a flight" when no rows are chosen
- App permissions and object-level permissions are configured separately
