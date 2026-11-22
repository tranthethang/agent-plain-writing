## Staging PostgreSQL maintenance

On 2026-12-03 at 04:00 UTC, the `db-stage-02` staging cluster will move from 16 GB to 32 GB of RAM.

The resize will cause 8 minutes of downtime. Staging connections will drop, and queued CI jobs will retry after 30 seconds.

Connection strings and credentials will stay unchanged.