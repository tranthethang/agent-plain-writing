### Staging database maintenance: `db-stage-02`

On 2026-12-03 at 04:00 UTC, the staging PostgreSQL cluster `db-stage-02` will be resized from 16 GB to 32 GB of RAM. The resize will take 8 minutes, with downtime expected from 04:00 to 04:08 UTC.

Staging connections will drop during the resize. Queued CI jobs will retry after 30 seconds. Connection strings and credentials will remain unchanged.