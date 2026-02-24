import streamlit as st
from reasoning_engine import ReasoningEngine
from policy_engine import PolicyEngine
from executor import Executor
import os

# Ensure folders exist
os.makedirs("workspace/moduleA/", exist_ok=True)
os.makedirs("workspace/protected/", exist_ok=True)

st.title("SafeDev Agent – Intent Aware AI Agent")

user_input = st.text_input("Enter instruction:")

if st.button("Run Agent"):
    if user_input:
        intent = ReasoningEngine.interpret(user_input)

        st.write("### Generated Intent:")
        st.write(intent)

        allowed, reason = PolicyEngine.validate(intent)

        st.write("### Policy Check:")
        st.write(reason)

        if not allowed:
            st.error("Execution Blocked.")
        else:
            result = Executor.execute(intent)
            st.success(result)
            