def detect_bias_flags(resume, jd):
    flags = []

    if resume.career_gaps:
        flags.append("Career gap detected (not penalized)")

    if jd.education_requirement:
        flags.append("Education requirement treated as flexible")

    return flags
