
# INC-003 — The Vanishing Backups

**Area:** Linux / Permissions
**Status:** Resolved

### Problem
MyApp failed to start as `appuser`.

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
