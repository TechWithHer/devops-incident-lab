Backup Cron Job Not Running

Area: Linux / Cron / Backup
Status: Resolved

Problem

Daily backups had stopped being created.

Investigation

Checked:

ls -lh /var/backups/daily/

Confirmed that no recent backup existed.

Investigated:

Cron configuration
Backup script
Script permissions
Script execution
Backup destination
Root Cause

The cron job had an issue preventing the backup script from executing successfully.

Fix

Corrected the underlying cron/script issue.

Verification

Executed the backup and confirmed a new file appeared in:

/var/backups/daily/
Learning

For scheduled jobs:

Cron
 ↓
Script
 ↓
Permissions
 ↓
Dependencies
 ↓
Output

Don't assume that a running cron service means the job itself is working.
