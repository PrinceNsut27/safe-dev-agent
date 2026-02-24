from intent_model import Intent


class ReasoningEngine:

    @staticmethod
    def interpret(user_input: str) -> Intent:

        if "create" in user_input:
            return Intent(
                action="create_file",
                target_path="workspace/moduleA/demo.txt",
                content="Hello from SafeDev Agent\n"
            )

        if "delete" in user_input:
            return Intent(
                action="delete_file",
                target_path="workspace/moduleA/demo.txt"
            )

        if "protected" in user_input:
            return Intent(
                action="create_file",
                target_path="workspace/protected/secret.txt",
                content="Trying to write in protected directory"
            )

        return Intent(
            action="create_file",
            target_path="workspace/moduleA/default.txt",
            content="Default action executed"
        )