# Repository Metrics

This folder contains daily metrics collected from the GitHub repository using GitHub Actions.

## Files

### clone_count.csv

Daily clone statistics including:

- **Date**: Timestamp when the data was collected (UTC)
- **Total Clones**: Total number of clones in the last 14 days
- **Unique Clones**: Number of unique users who cloned the repository in the last 14 days

### view_count.csv

Daily view statistics including:

- **Date**: Timestamp when the data was collected (UTC)
- **Total Views**: Total number of page views in the last 14 days
- **Unique Visitors**: Number of unique visitors in the last 14 days

### referrer_stats.csv

Daily referrer statistics including:

- **Date**: Timestamp when the data was collected (UTC)
- **Referrer**: The referring site (e.g., github.com, google.com, direct)
- **Count**: Number of views from this referrer
- **Uniques**: Number of unique visitors from this referrer

## Collection Schedule

The metrics are automatically collected daily at 6:00 AM UTC via GitHub Actions. The workflow:

1. Fetches traffic data from GitHub's API
2. Appends new data to the CSV files
3. Commits and pushes the updated files to the repository

## Manual Collection

You can also manually trigger the metrics collection by going to the "Actions" tab in GitHub and running the "Collect Repository Metrics" workflow.

## Notes

- GitHub's traffic API only provides data for the last 14 days
- The metrics represent cumulative data for the 14-day window at the time of collection
- All timestamps are in UTC format
- If there are no referrers for a given day, a "no-referrers" entry will be added
