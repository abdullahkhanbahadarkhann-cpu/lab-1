
def scholarship_review(
    score,
    documents_complete,
    identity_verified,
    income_proof_attached
):
    if (
        score >= 70
        and documents_complete
        and identity_verified
        and income_proof_attached
    ):
        return "Review"
    else:
        return "Hold"


test_cases = [
    {
        "name": "Pass Case",
        "input": (82, True, True, True),
        "expected": "Review",
        "reason": "All four conditions are satisfied."
    },
    {
        "name": "Identity Verification Failure",
        "input": (82, True, False, True),
        "expected": "Hold",
        "reason": "Identity verification is False."
    },
    {
        "name": "Income Proof Failure",
        "input": (82, True, True, False),
        "expected": "Hold",
        "reason": "Income proof is missing."
    },
    {
        "name": "Threshold Boundary",
        "input": (70, True, True, True),
        "expected": "Review",
        "reason": "A score of exactly 70 satisfies score >= 70."
    }
]

for case in test_cases:
    actual = scholarship_review(*case["input"])

    print("Test:", case["name"])
    print("Input:", case["input"])
    print("Expected:", case["expected"])
    print("Actual:", actual)
    print("Reason:", case["reason"])
    print("Result:", "PASS" if actual == case["expected"] else "FAIL")
    print("-" * 40)