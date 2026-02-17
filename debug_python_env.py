import os

print("--- Python Environment Variable Debug ---")
keys = ["ALFA_HOST", "ALFA_USER", "ALFA_PASS", "ALFA_PATH", 
        "SHINY_HOST", "SHINY_USER", "SHINY_PASS", "SHINY_PATH_1", "SHINY_PATH_2"]

with open("debug_env.txt", "w") as f:
    f.write("--- Python Environment Variable Debug ---\n")
    for key in keys:
        val = os.environ.get(key)
        if val:
            if "PASS" in key:
                f.write(f"{key}: [SET] (Length: {len(val)})\n")
            else:
                f.write(f"{key}: {val}\n")
        else:
            f.write(f"{key}: [MISSING]\n")
    f.write("---------------------------------------\n")
print("Written to debug_env.txt")
