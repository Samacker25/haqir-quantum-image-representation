def select_encoding(score, t1=0.02, t2=0.005):
    if score >= t1:
        return "HIGH"
    elif score >= t2:
        return "MEDIUM"
    else:
        return "LOW"