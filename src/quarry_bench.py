"""Quarry Bench: a replayable workload driver."""

import json
import time


def load_cases(path):
    with open(path, encoding='utf-8') as handle:
        return json.load(handle)['cases']


def run_case(engine, case):
    started = time.perf_counter()
    engine.execute(case['sql'])
    elapsed = time.perf_counter() - started
    return {'name': case['name'], 'elapsed_ms': round(elapsed * 1000, 2)}


def score(results):
    total = sum(row['elapsed_ms'] for row in results)
    return {'cases': len(results), 'total_ms': round(total, 2)}
