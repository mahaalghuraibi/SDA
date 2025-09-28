<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

## Morning Activity

This morning we will check to ensure that your install of postgreSQL was successful from Installfest in the first week.

## MacOS
1. Open Terminal and try:
   - `psql --version`  
     OR  
     `psql` (if you see a `postgres=#` prompt, PostgreSQL is installed; exit with `\q`)
2. If installed via Homebrew, you can also check:
   - `brew list` (look for postgresql)
   - `brew info postgresql`
3. Make sure you can enter the shell:
   - `psql -U postgres`

## Ubuntu
1. Open Terminal and try:
   - `psql --version`
   - or `psql` (see if prompt appears; exit with `\q`)
2. Check service status:
   - `systemctl status postgresql`  
     or `service postgresql status`
3. Make sure you can enter the shell:
   - `psql -U postgres`

