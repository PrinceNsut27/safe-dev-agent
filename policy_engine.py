from config import ALLOWED_DIRECTORY, PROTECTED_DIRECTORY, BLOCKED_COMMANDS


class PolicyEngine:

    @staticmethod
    def validate(intent):

        if intent.target_path.startswith(PROTECTED_DIRECTORY):
            return False, "Access to protected directory is blocked."

        if not intent.target_path.startswith(ALLOWED_DIRECTORY):
            return False, "File access outside allowed module."

        if intent.action == "delete_file":
            return False, "File deletion is not allowed."

        if intent.action == "run_command":
            for blocked in BLOCKED_COMMANDS:
                if blocked in intent.command:
                    return False, f"Blocked dangerous command: {blocked}"

        return True, "Intent validated successfully."