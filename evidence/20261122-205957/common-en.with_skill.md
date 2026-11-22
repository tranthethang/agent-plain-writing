## Staging PostgreSQL maintenance

The `db-stage-02` cluster will move from 16 GB to 32 GB of RAM on 2026-12-03 at 04:00 UTC.

Downtime will last 8 minutes. Staging connections will drop during the resize, and queued CI jobs will retry after 30 seconds. Connection strings and credentials will stay unchanged.