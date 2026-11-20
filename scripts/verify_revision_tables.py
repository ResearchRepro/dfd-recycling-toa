from pathlib import Path
import pandas as pd
r=Path(__file__).resolve().parents[1]/"results"/"revision_validation"
s=pd.read_csv(r/"validation_summary.csv")
t=s[s["file"].eq("core_random_300.csv") & s["variable"].eq("gold_function")].iloc[0]
assert int(t["agreed"])==250 and int(t["n"])==300
a=pd.read_csv(r/"05_function_gate_threshold_and_margin_sensitivity.csv")
b=a[(a.sim_threshold.round(3)==0.375) & (a.margin_threshold.round(2)==0.00)].iloc[0]
assert int(b["final_field_function"])==347
print("Aggregate checks passed: 250/300 expert function agreement; 347 original assignments")
