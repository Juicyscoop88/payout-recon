## Working with agents here

- Every change starts from a short spec: what, why, and one example with its expected result, in the issue or
  the pull request description. The tester writes its tests from it without seeing the code; the gate asks
  for it when it is missing.
- Long work goes in small pull requests merged along the way, each one change with its why. Never one big
  pull request at the end.
- Write progress down where the next session finds it: the pull request description, or the task file of
  `/four-eyes:ship`. A new session reads it first.
- The gate in CI is the check, whoever wrote the code: blind tests, the protected tests, and the questions only a
  person can answer. Run `/code-review` before a push if you like; it does not replace the gate.
- Hand a larger change to the factory with `/four-eyes:ship <what and why>`, or work with Claude as usual.
