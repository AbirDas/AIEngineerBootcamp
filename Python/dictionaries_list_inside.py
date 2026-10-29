
bhakts = {
    "Hanuman": ["Selfless Service", "Complete Surrender", "infinite strength", "wisdom", "unique ability to completely eliminate his ego", "My everything"],
    "Lakshmana": ["Devoted Brother", "Sacrifice", "Constant Protection"],
    "Shabari": ["Patient Ascetic", "Unwavering Faith", "Pure Love"]
}

for bhakt, qualities in bhakts.items():
    print(f" {bhakt} has the unique qualites")
    for qualitie in qualities:
        print(f"-{qualitie}")
    print()