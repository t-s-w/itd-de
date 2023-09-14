# itd-de

Take-home assignment for EDB ITD.

## Problem Task

Given the Github API (https://docs.github.com/en/free-pro-team@latest/rest), create a simple ETL pipeline.

For a particular repository, example Airflow (https://github.com/apache/airflow), pull in the commits over the last 6 months.

With the data ingested, address the follow queries:

- For the ingested commits, determine the top 5 committers ranked by count of commits and their number of commits.
- For the ingested commits, determine the committer with the longest commit streak.
- For the ingested commits, generate a heatmap of number of commits count by all users by day of the week and by 3 hour blocks.

## System Requirements

Docker must be installed on the system.

## Loading scripts

Navigate to the root of this repository after cloning it onto your system, then run:

`docker compose up -d`

This will:

- Deploy a local postgres database at port 5432
- Run an ETL script that fetches the data from GitHub commits API, and loads it into the Postgres database
- Deploy a local Jupyter Notebook instance at port 8888

To see the data visualisations, go to `https://localhost:8888` and type in the password found in `${NOTEBOOK_PW}` in the `.env` file.

## Environment Variables

For the purposes of this assignment, ease of deployment was prioritised over security, so all services are local, and the `.env` file is provided in the repo.

The variables are:

- `NOTEBOOK_PW` - security token to log in to the Jupyter Notebook instance
- `PG_*` - Variables for the Postgres instance; username, password (both for loading script and to access the database), hostname and database name
- `REPO` - GitHub repository whose commits are to be analysed. The `.env` provided defaults to `apache/airflow` as suggested
