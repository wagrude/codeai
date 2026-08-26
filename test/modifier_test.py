from src.modifier import (
    propose_change,
    apply_proposed_change
)


file_path = "test/edit_target.c"

instruction = (
    "Change the add function so it returns "
    "a + b + 30."
)

old_content, new_content, diff = propose_change(
    file_path,
    instruction
)

apply_proposed_change(
    file_path,
    old_content,
    new_content,
    diff
)
