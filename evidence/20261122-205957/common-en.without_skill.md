### Staging PostgreSQL maintenance: `db-stage-02`

On 2026-12-03 at 04:00 UTC, the staging cluster will be resized from 16 GB to 32 GB of RAM. The maintenance will take 8 minutes.

During this downtime, staging connections will drop. Queued CI jobs will retry after 30 seconds. Connection strings and credentials will remain unchanged.