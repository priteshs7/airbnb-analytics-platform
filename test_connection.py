import snowflake.connector

try:
    conn = snowflake.connector.connect(
        user="PRESET_APP",
        password="presetPassword123",
        account="dcllfsu-fk70220",
        warehouse="COMPUTE_WH",
        database="AIRBNB",
        schema="DEV",
        role="REPORTER"
    )

    print("✅ Connected successfully!")

    cur = conn.cursor()
    cur.execute("""
        SELECT CURRENT_USER(),
               CURRENT_ROLE(),
               CURRENT_WAREHOUSE(),
               CURRENT_DATABASE(),
               CURRENT_SCHEMA();
    """)

    for row in cur:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection failed")
    print(e)