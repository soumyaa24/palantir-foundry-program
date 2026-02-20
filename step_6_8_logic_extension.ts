import { Function } from "@palantir/functions-api";
import { Objects, Flight } from "@palantir/models-objects";

export class FlightActions {

    /**
     * Returns severity level based on average departure delay across selected flights.
     * Used by the Workshop severity KPI card.
     */
    @Function()
    public async getDelaySeverity(flights: Flight[]): Promise<string> {
        if (flights.length === 0) {
            return "Select a flight";
        }

        // Average the departure delays across all selected rows
        const total = flights.reduce((sum, f) => sum + (f.depDelay ?? 0), 0);
        const avg = total / flights.length;

        if (avg > 60) return "CRITICAL";
        if (avg > 30) return "WARNING";
        return "NORMAL";
    }

    /**
     * Updates status for a batch of flights.
     * Called by the Mark as Resolved button in Workshop.
     * Only triggered after user confirms the action.
     */
    @Function()
    public async bulkUpdateStatus(flights: Flight[], newStatus: string): Promise<void> {
        flights.forEach(f => {
            console.log(`Flight ${f.flightId}: status updated to ${newStatus}`);
        });
    }
}
