# Step 7 - AIP Logic Agent

**Agent Name**: Flight Delay Assistant

An AIP Logic agent embedded in the Workshop app. Instead of building a new form for every operational use case, the agent handles natural language questions and governed write actions.

## What I Did

- Created agent: Flight Delay Assistant in AIP Logic
- Wrote system prompt defining role and constraints
- Connected two tools: getDelaySeverity (read) and bulkUpdateStatus (write)
- Tested read queries and write actions with confirmation flow
- Embedded in Workshop via AIP Chat widget

### What Was Automated

1. Read queries â€” "Which AA flights are critical?" calls getDelaySeverity on filtered Flight objects
2. Write actions â€” "Mark all critical UA flights as resolved" asks for confirmation, then calls bulkUpdateStatus

### Where Logic Was Used

Logic runs within Foundry governance:
- Agent reads from Flight Ontology objects, not raw datasets
- Write actions go through TypeScript Functions â€” audited and permission-checked
- Agent cannot bypass object-level permissions

## Creating the Agent

1. Open AIP Logic from Foundry sidebar
2. Click + New Agent
3. Name: Flight Delay Assistant

## System Prompt

```
You are a flight operations assistant with access to live flight data through the Foundry Ontology.

You can:
- Look up delayed flights and their current severity
- Recommend RESOLVED or ESCALATED status for flights
- Call bulkUpdateStatus only when the user explicitly confirms

Keep responses concise. Always confirm before taking write actions.
```

## Tools

### getDelaySeverity
- Type: Ontology Function
- Returns: NORMAL, WARNING, or CRITICAL

### bulkUpdateStatus
- Type: Ontology Function
- Action: Updates flight status â€” only after user confirmation

## Testing

Read query:
```
Which AA flights are in a critical situation right now?
```
Result: Agent calls getDelaySeverity, returns breakdown

Write action:
```
Mark all critical UA flights as RESOLVED.
```
Result: Agent confirms count, then calls bulkUpdateStatus

## What I Learned

- System prompt took three rewrites â€” first version triggered write actions without confirmation
- Tool calling must be designed carefully: read tools are always safe, write tools need explicit confirmation logic in the prompt
- The agent respects Ontology permissions â€” unauthorized users cannot trigger bulkUpdateStatus even if they ask
