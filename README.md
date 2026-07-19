# Airbnb Analytics Platform

An end-to-end data engineering project built with **Snowflake**, **dbt**, and **Preset** to transform Airbnb listing and review data into analytics-ready models and interactive dashboards.

## Tech Stack

- Snowflake
- dbt Core
- SQL
- Jinja
- Preset (Apache Superset)
- Git & GitHub

## Project Structure

```
models/
├── src/        # Source models
├── dim/        # Dimension models
├── fct/        # Fact models
└── mart/       # Business-ready marts

tests/          # Custom & generic tests
macros/         # Reusable dbt macros
seeds/          # Seed data
snapshots/      # Slowly changing dimensions
analyses/       # Analysis queries
assets/         # Documentation images
```

## Pipeline

Raw Airbnb Data
→ Source Models
→ Dimension Models
→ Fact Models
→ Mart Models
→ Preset Dashboard

## Features

- Source, Dimension, Fact and Mart models
- Custom and generic dbt tests
- Snapshots
- Seeds
- Reusable macros
- dbt documentation
- Interactive dashboard in Preset
- Snowflake integration

## Dashboard

The project includes an Executive Dashboard built in Preset for Airbnb listings, bookings and review analytics.

## Run Locally

```bash
dbt deps
dbt seed
dbt run
dbt test
dbt docs generate
dbt docs serve
```

## Author

**Pritesh S**