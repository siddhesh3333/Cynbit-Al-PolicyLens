import json
import unittest

from checker import parse_result, validate_input


class CheckerTests(unittest.TestCase):
    def test_validate_input_reports_missing_fields(self):
        errors = validate_input("", "question", "draft", "model")
        self.assertIn("Please enter the official company policy.", errors)

    def test_validate_input_rejects_oversized_field(self):
        errors = validate_input("x" * 12001, "q", "d", "model")
        self.assertTrue(any("12,000" in error for error in errors))

    def test_parse_valid_result(self):
        payload = {
            "status": "Contradiction",
            "reason": "The timeline does not match the policy.",
            "supported_points": [],
            "unsupported_claims": ["Refund tomorrow"],
            "contradictions": ["30-day return window"],
            "safer_reply": "The policy allows returns within 14 days. Please contact support if you need an exception.",
        }
        self.assertEqual(parse_result(json.dumps(payload))["status"], "Contradiction")

    def test_parse_rejects_unknown_status(self):
        payload = {
            "status": "Approved",
            "reason": "ok",
            "supported_points": [],
            "unsupported_claims": [],
            "contradictions": [],
            "safer_reply": "ok",
        }
        with self.assertRaises(ValueError):
            parse_result(json.dumps(payload))

    def test_parse_rejects_malformed_json(self):
        with self.assertRaises(ValueError):
            parse_result("not json")

    def test_parse_requires_array_fields(self):
        payload = {
            "status": "Supported",
            "reason": "ok",
            "supported_points": "not a list",
            "unsupported_claims": [],
            "contradictions": [],
            "safer_reply": "ok",
        }
        with self.assertRaises(ValueError):
            parse_result(json.dumps(payload))

    def test_check_reply_rejects_missing_api_key_before_importing_sdk(self):
        from checker import check_reply

        with self.assertRaisesRegex(ValueError, "Groq API key is required"):
            check_reply("policy", "question", "draft", "", "model")


if __name__ == "__main__":
    unittest.main()
