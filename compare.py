scheme_data = {

    "PMEGP": {
        "Loan Limit": "50 Lakh",
        "Subsidy": "Yes",
        "Target": "Entrepreneurs"
    },

    "Mudra Loan": {
        "Loan Limit": "20 Lakh",
        "Subsidy": "No",
        "Target": "Small Business"
    },

    "PM Kisan": {
        "Benefit": "₹6000/year",
        "Target": "Farmers"
    }
}


def compare_schemes(
        scheme1,
        scheme2
):

    if scheme1 not in scheme_data:
        return None

    if scheme2 not in scheme_data:
        return None

    return {
        scheme1: scheme_data[scheme1],
        scheme2: scheme_data[scheme2]
    }