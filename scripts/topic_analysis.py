def tag_headline(text):
    text = text.lower()
    if "product" in text or "launch" in text or "unveil" in text:
        return "Product"
    elif "record" in text or "high" in text or "growth" in text:
        return "Performance"
    elif "concerns" in text or "lawsuit" in text or "drop" in text:
        return "Risk"
    elif "merger" in text or "acquisition" in text:
        return "Corporate Action"
    else:
        return "Other"
