# AI Residency — Meet the Builders

A single-page, mobile-first site for the IIMA Ventures AI Summer Residency x entreVC x Prodman event (27 June). Teams are grouped by sector; tap **Read more** on any team to see their full problem and solution.

## Files
- `index.html` — the site (self-contained, data is embedded; just open it).
- `data.json` — the team data (source for the embedded copy).
- `build_data.py` — regenerates `data.json` from `Cohort AI Residency-final.xlsx`.
- `build_html.py` — regenerates `index.html` from `data.json`.

## Backfilling room numbers
Easiest: edit `data.json`, set each team's `"room"` (e.g. `"room": "Room 4"`), then run:

```
python3 build_html.py
```

(Or edit the `"room"` values directly inside the `<script type="application/json">` block in `index.html`.)
