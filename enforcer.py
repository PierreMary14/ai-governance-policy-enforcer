import json

def check_policy(config):
    policies = {
        "data_retention_days": 30,
        "pii_redaction": True,
        "max_token_cost": 0.05
    }
    
    violations = []
    if config.get("retention") > policies["data_retention_days"]:
        violations.append("Data retention exceeds 30 days.")
    if not config.get("redaction"):
        violations.append("PII redaction is disabled.")
        
    return violations

# Mock LLM Config
llm_config = {
    "model": "gpt-4",
    "retention": 60,
    "redaction": False
}

print("AI Center of Excellence: Running Governance Audit...")
violations = check_policy(llm_config)

if violations:
    print(f"Policy Violations Found: {violations}")
else:
    print("AI Configuration is compliant.")