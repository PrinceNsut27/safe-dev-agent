# SafeDev Agent

SafeDev Agent is an intent-aware autonomous system designed to demonstrate strict alignment between reasoning and execution.

## Objective

To ensure that autonomous agents operate within user-defined constraints and prevent unintended system modifications.

---

## Architecture Overview

The system consists of four core components:

1. **Reasoning Engine**
   - Converts user instruction into structured intent.
   - No execution happens here.

2. **Intent Model**
   - Structured schema using Pydantic.
   - Prevents ambiguous actions.

3. **Policy Engine**
   - Validates intent against enforceable constraints.
   - Blocks unauthorized actions deterministically.

4. **Execution Engine**
   - Executes actions only after policy approval.

5. **Logger**
   - Provides traceability and runtime logs.

---

## Enforcement Model

The system enforces:

- Directory-scoped access control
- Blocked actions (e.g., file deletion)
- Protected directory restrictions
- Command blacklist enforcement

Execution is impossible without successful validation.

---

## Demonstrated Behavior

### Allowed Action
create file → File created successfully

### Blocked Action
delete file → Execution blocked by policy

---

## How to Run

```bash
pip install -r requirements.txt
python main.py