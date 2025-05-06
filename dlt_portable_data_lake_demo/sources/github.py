import gzip
from typing import Iterator

import dlt
from dlt.common import json
from dlt.sources import DltResource, TDataItems


@dlt.source
def github_event(
    archive: str = dlt.config.value, max_events: int = 10000, chunksize: int = 1000
) -> DltResource:
    """Dispatches a stream of github events to Delta tables by event type. Partitions data
    on _dlt_load_id to make incremental transformations efficient.
    """

    @dlt.resource(
        primary_key="id",
        table_name=lambda i: i["type"],
        # table_format="delta",  # no longer needed, iceberg will force iceberg tables
        write_disposition="append",
        columns={"_dlt_load_id": {"partition": True}},
    )
    def event() -> Iterator[TDataItems]:
        with gzip.open(archive, "rb") as f:
            f.seek(dlt.current.resource_state().setdefault("pos", 0))
            chunk = []
            for line_no, line in enumerate(f):
                chunk.append(json.loadb(line))
                if (line_no + 1) >= max_events:
                    break
                if len(chunk) >= chunksize:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk
            dlt.current.resource_state()["pos"] = f.tell()

    return event
