# SafeDev Agent – Project Documentation

## 1. Intent Model

The system uses a structured Intent model built using Pydantic.

Each user instruction is converted into:
- action
- target_path
- content
- command

This prevents ambiguous execution and ensures deterministic interpretation.

---

## 2. Policy Model

The Policy Engine enforces:

- Directory-scoped access control
- Protected directory restriction
- Blocked file deletion
- Command blacklist enforcement

All constraints are checked before execution.

---

## 3. Enforcement Mechanism

The system strictly separates reasoning from execution.

Flow:

User Input  
↓  
Reasoning Engine  
↓  
Structured Intent  
↓  
Policy Engine (Validation Layer)  
↓  
Execution Engine  

If validation fails, execution is blocked.

The execution layer cannot be accessed directly.

---

## 4. Allowed Action Demonstration

Input:
create file

Result:
Intent validated successfully.
File created successfully.

---

## 5. Blocked Action Demonstration

Input:
delete file

Result:
File deletion is not allowed.
Execution Blocked.

---

## 6. Architectural Principle

The system enforces:

Separation between reasoning and execution with deterministic runtime policy enforcement.