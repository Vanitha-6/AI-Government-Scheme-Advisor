def recommend_schemes(
        age,
        occupation,
        income
):

    schemes = []

    if occupation == "Student":

        schemes.extend([
            "National Scholarship Portal",
            "AICTE Scholarship",
            "Skill India"
        ])

    elif occupation == "Farmer":

        schemes.extend([
            "PM Kisan",
            "PMEGP",
            "Mudra Loan"
        ])

    elif occupation == "Business Owner":

        schemes.extend([
            "Mudra Loan",
            "PMEGP",
            "Stand Up India"
        ])

    elif occupation == "Employee":

        schemes.extend([
            "ESI",
            "APY",
            "NCS"
        ])

    else:

        schemes.extend([
            "Skill India",
            "Mudra Loan"
        ])

    return schemes