# OreConcentrate_RESTAPI

---
## CLI
<details>
<summary>CREATING DATABASE</summary>

**Simple command line interface, that:**

1) allows you to create db:
   ``` commandline
   python -m src.db --create_db
   ```
2) allows you to drop db:
   ``` commandline
   python -m src.db --drop_db
   ```
3) And contains optional arguments:
    - `-d`, `--db_name`, allows assign db name:
   
        ``` commandline
        python -m src.db --drop_db -d your_db_name
        ```

    - `-u`, `--user_name`, allows assign username:
   
        ``` commandline
        python -m src.db --create_db -u your_user_name
        ```
    
    - `-r`, `--role_name`, allows assign role name:
   
        ``` commandline
        python -m src.db --create_db -r your_role_name
        ```
    
    - `-p`, `--user_password`, allows assign user password:
   
        ``` commandline
        python -m src.db --create_db -p your_user_password
        ```
4) Helper:
    ``` commandline
    python -m src.db -h
    ```

**IMPORTANT:** **If the arguments is not specified, it is taken from the env variables.**
</details>

<details>
<summary>POPULATING DATABASE</summary>

1) Populate the empty database with prepared data.:
   ``` commandline
   python -m src.utils.db_populating --populate_db
   ```
2) Helper:
    ``` commandline
    python -m src.utils.db_populating -h
    ```
</details>