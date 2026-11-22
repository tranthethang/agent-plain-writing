---
lang: en
type: common
non_tech: false
---

# SIMULATED DATA

## Audience

Backend engineers reading an internal maintenance notice in the platform changelog.

## Brief

### Summary
The staging PostgreSQL cluster (`db-stage-02`) moves from 16 GB to 32 GB of RAM on 2026-12-03 at 04:00 UTC. The resize takes 8 minutes, during which staging connections drop and queued CI jobs retry after 30 seconds. Connection strings and credentials stay unchanged.

### Reader
Backend engineers who run integration tests against staging and need the exact window and impact.

### Words to use or avoid
- Use: `staging`, `cluster`, `downtime`.
- Avoid: `seamless`, `leverage`, `synergy`, `we`, `our`.

## Facts
- Cluster name: `db-stage-02`
- Database engine: PostgreSQL
- RAM change: 16 GB to 32 GB
- Maintenance window: 2026-12-03 at 04:00 UTC
- Duration: 8 minutes
- CI retry delay: 30 seconds
