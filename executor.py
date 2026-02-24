import subprocess


class Executor:

    @staticmethod
    def execute(intent):

        if intent.action == "create_file":
            with open(intent.target_path, "w") as f:
                f.write(intent.content or "")
            return "File created successfully."

        elif intent.action == "edit_file":
            with open(intent.target_path, "a") as f:
                f.write(intent.content or "")
            return "File edited successfully."

        elif intent.action == "run_command":
            result = subprocess.run(intent.command, shell=True, capture_output=True, text=True)
            return result.stdout

        else:
            return "Unsupported action."