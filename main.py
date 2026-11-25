import os

# Verified count: 108 characters (108 bytes UTF-8).
LINE = "Our standup lasted two hours. Nobody stood up, and nothing got done, but the calendar says we are agile now."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
output_path = os.path.join(output_dir, "entry.txt") if output_dir else "/output/entry.txt"

with open(output_path, "w", encoding="utf-8", newline="") as fh:
    fh.write(LINE)

print(len(LINE))
