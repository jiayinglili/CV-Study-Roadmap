raw_data = [0.95,0.1,None,0.88,0.05,"error",0.6]
clean_scores = []
#Filter
for x in raw_data:
    if isinstance(x,float) and x > 0.5:
        x*=100
        clean_scores.append(x)
# Map
print(clean_scores)