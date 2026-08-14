# INC-001 — What is writing to this log file?

**Area:** Linux 
**Status:** Resolved

### Problem
A developer created a testing program that is continuously writing to a log file /var/log/bad.log and filling up disk. You can check for example with tail -f /var/log/bad.log.
This program is no longer needed. Find it and terminate it. Do not delete the log file.

### Investigation
- Checked user → `appuser`
- Checked file → `root:root`
- Checked permissions → no `x`
- Tested startup → `Permission denied`

### Root Cause
`start.sh` was not executable by `appuser`.

### Fix
Added required execute permission.

### Verification
Application started successfully as `appuser`.

### Learning
Check ownership and permissions when an application returns `Permission denied`.
