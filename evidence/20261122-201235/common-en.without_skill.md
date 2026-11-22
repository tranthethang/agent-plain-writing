### Staging PostgreSQL maintenance

On 2026-12-03 at 04:00 UTC, cluster `db-stage-02` will be resized from 16 GB to 32 GB of RAM. The maintenance will take 8 minutes, during which staging connections will drop. Queued CI jobs will retry after 30 seconds.

Connection strings and credentials will remain unchanged.