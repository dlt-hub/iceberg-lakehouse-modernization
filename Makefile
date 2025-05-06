dev:
	uv sync --reinstall-package dlt --upgrade-package dlt --reinstall-package dlt-plus --upgrade-package dlt-plus --all-extras --group dev --no-managed-python

test:
	uv run pytest

run: download-gh
	dlt project clean
	dlt pipeline -l
	dlt pipeline events_to_lake run
	dlt dataset github_events_dataset row-counts
	dlt transformation . run
	dlt dataset reports_dataset info
	dlt dataset reports_dataset row-counts

run-cont:
	dlt dataset github_events_dataset row-counts
	dlt transformation . run
	dlt dataset reports_dataset info
	dlt dataset reports_dataset row-counts

download-gh:
	mkdir -p dlt_portable_data_lake_demo/_data
	cd dlt_portable_data_lake_demo/_data && wget https://data.gharchive.org/2024-10-13-15.json.gz

.PHONY: tests