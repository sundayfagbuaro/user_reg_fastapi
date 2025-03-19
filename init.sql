CREATE USER appadmin with ENCRYPTED PASSWORD 'Superadminuser';
  ALTER ROLE appadmin WITH SUPERUSER;
  CREATE DATABASE users_db;
  grant all privileges on database users_db to appadmin
