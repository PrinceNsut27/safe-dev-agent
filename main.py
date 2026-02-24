import os
from reasoning_engine import ReasoningEngine
from policy_engine import PolicyEngine
from executor import Executor
from logger import log


def ensure_workspace():
    os.makedirs("workspace/moduleA/", exist_ok=True)
    os.makedirs("workspace/protected/", exist_ok=True)


def main():
    ensure_workspace()

    user_input = input("Enter instruction: ")

    # Step 1: Reasoning
    intent = ReasoningEngine.interpret(user_input)
    log(f"Generated Intent: {intent}")

    # Step 2: Policy Validation
    allowed, reason = PolicyEngine.validate(intent)
    log(f"Policy Check: {reason}")

    if not allowed:
        log("Execution Blocked.")
        return

    # Step 3: Execution
    result = Executor.execute(intent)
    log(f"Execution Result: {result}")


if __name__ == "__main__":
    main()