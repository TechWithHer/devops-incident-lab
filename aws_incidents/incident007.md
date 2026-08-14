INC-005 — EKS Latency and ALB 5xx Errors

Area: AWS / EKS / Observability
Severity: High
Status: Resolved

Problem

After a routine application deployment:

p95 latency increased
ALB 5xx errors increased
HPA scaled aggressively
Pods remained healthy
CPU/memory remained normal
Investigation

Used:

CloudWatch
kubectl logs
Prometheus
Grafana
Application traces

Traces showed delays in ElastiCache/Redis calls.

Root Cause

A new application change introduced a blocking Redis call without proper timeout handling.

Redis delay
    ↓
Thread pool exhaustion
    ↓
Request backlog
    ↓
ALB timeout
    ↓
5xx errors
Mitigation
Rolled back Helm deployment
Restarted affected pods
Stabilized HPA/connection limits
Monitored latency and errors
Permanent Fix
Redis timeouts
Fallback caching
Connection pool improvements
Circuit breaker
Dependency-latency monitoring
Learning

Healthy pods do not necessarily mean a healthy application.

Always investigate downstream dependencies when infrastructure metrics look normal.
