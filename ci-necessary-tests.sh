#!/bin/bash

# List of test files to run
test_files=(
    "tests/test_behavioral_assert/test_behavioral_assert_basic.py"
    "tests/test_behavioral_assert/test_behavioral_assert_complex.py"
    "tests/test_behavioral_assert/test_behavioral_assert_configuration.py"
    "tests/test_behavioral_assert/test_behavioral_assert_llm_injection.py"
    "tests/test_behavioral_assert/test_behavioral_assert_prompt_configurator.py"
    "tests/test_behavioral_assert/test_behavioral_assert_validations.py"
)

# Array to store background process IDs
pids=()
# Variable to track test failures
failed=0

# Run each test file in parallel
for test_file in "${test_files[@]}"; do
    echo "Running tests in $test_file..."
    pytest "$test_file" &
    # Capture the PID of the background process
    pids+=($!)
done

# Wait for all background processes and check their exit status
for pid in "${pids[@]}"; do
    wait "$pid"
    status=$?
    if [ $status -ne 0 ]; then
        echo "Test failed for process ID $pid"
        failed=1
    fi
done

# Exit with an error code if any test failed
if [ $failed -ne 0 ]; then
    echo "One or more tests failed."
    exit 1
else
    echo "All tests passed!"
    exit 0
fi