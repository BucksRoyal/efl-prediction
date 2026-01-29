from datetime import date

# Start HTML
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>EFL League One Prediction</title>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        table {{ border-collapse: collapse; width: 70%; margin: auto; }}
        th, td {{ border: 1px solid #333; padding: 5px; text-align: center; }}
        th {{ background-color: #222; color: white; }}
        .playoff {{ background-color: #c6f6d5; }}
        .relegation {{ background-color: #fbb6b6; }}
    </style>
</head>
<body>
<h1>EFL League One – End of Season Prediction</h1>
<p>Simulation date: {date.today()}, Generated using Python</p>

<table>
<tr><th>Pos</th><th>Team</th><th>Projected Points</th></tr>
"""

# Table data
teams = [
    ("Lincoln City", 89),
    ("Cardiff City", 87),
    ("Bradford City", 84),
    ("Bolton Wanderers", 82),
    ("Stevenage", 78),
    ("Huddersfield Town", 74),
    ("Stockport County", 73),
    ("Wycombe Wanderers", 65),
    ("Reading", 64),
    ("Luton Town", 63),
    ("Barnsley", 62),
    ("Exeter City", 60),
    ("Mansfield Town", 59),
    ("Plymouth Argyle", 58),
    ("Peterborough United", 56),
    ("AFC Wimbledon", 52),
    ("Doncaster Rovers", 51),
    ("Northampton Town", 51),
    ("Blackpool", 50),
    ("Wigan Athletic", 49),
    ("Burton Albion", 49),
    ("Rotherham United", 48),
    ("Leyton Orient", 47),
    ("Port Vale", 33),
]

# Generate table rows
for i, (team, pts) in enumerate(teams, start=1):
    if i <= 6:
        cls = "playoff"
    elif i > 20:
        cls = "relegation"
    else:
        cls = ""
    html += f'<tr class="{cls}"><td>{i}</td><td>{team}</td><td>{pts}</td></tr>\n'

# Close HTML
html += "</table>\n</body>\n</html>"

# Save HTML file
with open("efl_prediction.html", "w") as f:
    f.write(html)

print("HTML file generated: efl_prediction.html")
