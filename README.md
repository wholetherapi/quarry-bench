# Quarry Bench

Replayable benchmark harness for comparing query engines.

## Release status

Released: v0.9.1 is publicly available from this repository.

## Usage

```
quarry-bench run --workload data/workloads.json --engine duckdb
```

## Layout

- `src/quarry_bench.py` — workload driver
- `data/bench_cases.json` — reference cases
- `experiments/results_2026.md` — published comparison results
