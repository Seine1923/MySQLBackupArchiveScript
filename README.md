MySQL DATABASE BACKUP AND ARCHIVE
===============================

This script implemented by python.

There are two features below show:  
1. Backup database. This script automatically generate direcctory like "20161019", and backup current mysql dababase into today's directory.  
2. Archive backup data. This script can archive all backup data except today into one single .tar.gz file.

DIRECTORY STRUCTURE
-------------------

```
dbbackup
	20161018							
		ttmgrportal20161018-181406.sql		backup file  ttmgrportal20161018-182156.sql		backup file
	20161019
		ttmgrportal20161019-134431.sql		backup file
	ttmgrportal.tar.gz						Archive file
```