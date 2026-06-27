import openpyxl, json

wb = openpyxl.load_workbook('Cohort AI Residency-final.xlsx', data_only=True)
ws = wb.active

def cell(r, c):
    v = ws.cell(row=r, column=c).value
    return ('' if v is None else str(v)).strip()

# Per-row curated keywords + a cleaned sector-group label.
# Keyed by row number (2..20). Source of truth for problem/solution/members/startup is the sheet itself.
meta = {
    2:  ("Space Tech",            ["SAR/InSAR radar", "Satellite compute", "Deformation maps"]),
    3:  ("Enterprise AI",         ["Field sales", "Voice intelligence", "Multilingual", "Privacy-first"]),
    4:  ("Fintech",               ["Loan collections", "Debt recovery", "NBFCs"]),
    5:  ("Consumer Tech",         ["Content engineering", "Low token cost"]),
    6:  ("Physical AI & Robotics",["Robotics data", "Multimodal sensing", "Embodied AI"]),
    7:  ("Healthtech",            ["Genomics", "Risk prediction", "India-specific"]),
    8:  ("Consumer Tech",         ["Creator economy", "Content workflow", "Brand matching"]),
    9:  ("Aerospace",             ["Industrial sensor data", "Physics-aware AI", "Failure modes"]),
    10: ("Consumer Tech",         ["Language learning", "Engagement", "Mobile app"]),
    11: ("Geospatial Tech",       ["Railway safety", "Satellite InSAR", "Ground deformation"]),
    12: ("Geospatial Tech",       ["Earth observation", "Developer API", "Geospatial infra"]),
    13: ("Enterprise AI",         ["Fleet safety", "Driver fatigue", "Edge AI"]),
    14: ("Consumer Tech",         ["D2C fashion", "Conversational commerce", "Ad conversion"]),
    15: ("Enterprise AI",         ["AI services", "D2C & SME", "Student teams"]),
    16: ("Enterprise AI",         ["Power grid", "Theft & loss", "Solar curtailment"]),
    17: ("Advanced Manufacturing",["Design feasibility", "Contract manufacturing", "Quoting"]),
    18: ("Fintech",               ["AML / RegTech", "Alert triage", "False positives"]),
    19: ("Consumer Tech",         ["English learning", "Short-form video"]),
    20: ("Regulatory Tech",       ["DPDP Act", "Compliance", "Automation"]),
}

# Display order of sector groups
group_order = [
    "Space Tech", "Aerospace", "Geospatial Tech", "Physical AI & Robotics",
    "Fintech", "Healthtech", "Enterprise AI", "Consumer Tech",
    "Advanced Manufacturing", "Regulatory Tech",
]

rows = []
for r in range(2, ws.max_row + 1):
    members = cell(r, 1)
    if not members:
        continue
    startup = cell(r, 2)
    rows.append({
        "room": "",
        "startup": startup,
        "members": members,
        "sector": meta[r][0],
        "keywords": meta[r][1],
        "problem": cell(r, 3),
        "solution": cell(r, 5),
    })

# Stable order: by group_order, preserving sheet order within a group
rows.sort(key=lambda x: group_order.index(x["sector"]))

out = {"groupOrder": group_order, "teams": rows}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("teams:", len(rows))
for g in group_order:
    n = [t["startup"] or t["members"] for t in rows if t["sector"] == g]
    print(f"  {g}: {len(n)} -> {n}")
