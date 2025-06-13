## Workflow: Add new feature [/feature]

**Prerequisites:** User has specified the feature requirements and target functionality

### Step 0: Initial Git Status Check

**[Mode: code]**

- Run `git status` to check current repository state
- Ensure working directory is clean or document existing changes
- **Success criteria:** Git status documented and ready for workflow

### Step 1: Analyze existing codebase

**[Mode: ask]**

- Search for similar functionality in `src/` directory using semantic search
- Identify patterns and conventions from existing code
- **Decision criteria:** If similar functionality exists, extend existing file; if not, create new file
- **On failure:** Ask user for clarification on feature requirements
- **Success criteria:** Clear understanding of implementation approach and file location

### Step 2: Create or modify implementation file

**[Mode: code]**

- Create new file `src/{feature-name}.ts` or modify existing file
- Implement feature following functional domain modeling principles
- Use `option-t` Result types for error handling
- **Prerequisites:** Step 1 completed successfully
- **On failure:** Switch to [Mode: debug] to analyze compilation errors
- **Success criteria:** File compiles without TypeScript errors

### Step 3: Create comprehensive test file

**[Mode: code]**

- Create `src/{feature-name}.test.ts` with unit tests
- Cover all code paths and edge cases
- Follow TDD principles with descriptive test names
- **Prerequisites:** Implementation file exists and compiles
- **On failure:** Switch to [Mode: debug] to fix test setup issues
- **Success criteria:** All tests pass with `bun test`

### Step 4: Lint validation

**[Mode: code]**

- Run `bun lint src/{feature-name}.ts`
- **Decision criteria:** If lint errors exist, fix them; if none, proceed
- **On failure:** Fix lint errors or switch to [Mode: refactor] for complex issues
- **Success criteria:** Zero lint errors reported

### Step 5: Integration testing

**[Mode: code]**

- Run `bun test` to ensure no regressions
- **Decision criteria:** If tests fail, determine if issue is in new code or existing code
- **On failure:** Switch to [Mode: debug] to identify and fix failing tests
- **Success criteria:** All tests pass including existing test suite

### Step 6: Final Git Commit

**[Mode: code]**

- Stage changes with `git add .`
- Commit with conventional commit message format:
  - `feat: add {feature-name}` for new features
  - `feat: extend {existing-feature}` for feature extensions
- **Prerequisites:** All tests pass and lint checks succeed
- **Success criteria:** Changes committed with appropriate conventional commit message

### Step 7: Transition to refactoring

**[Mode: orchestrator]**

- Delegate to "Single File Refactoring" workflow for code quality improvements
- **Prerequisites:** Changes committed successfully
- **Success criteria:** Workflow transition completed
