# config.py
DEFAULTS = {
    "mission": "Kepler",                # "Kepler"|"TESS"
    "min_period_days": 0.5,
    "max_period_days": 30.0,
    "duration_hours_candidates": [1.0, 2.0, 3.0],
    "flatten_window_length": 401,       # safe for Kepler long cadence
    "flatten_polyorder": 2,
    "quality_mask": "hard",             # "hard"|"soft"|None
    "offline_mode": True,               # prefer local files first
    "window_len": 2048,
    "window_stride": 256
}
