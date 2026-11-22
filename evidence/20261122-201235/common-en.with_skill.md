## Staging PostgreSQL maintenance

On 2026-12-03 at 04:00 UTC, the staging PostgreSQL cluster `db-stage-02` will move from 16 GB to 32 GB of RAM. The resize will take 8 minutes.

During this downtime, staging connections will drop. Queued CI jobs will retry after 30 seconds. Connection strings and credentials will stay unchanged.