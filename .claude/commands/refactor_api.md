## Workflow: Library API Refactoring [/refactor_api]

**Prerequisites:** Library has existing API and test suite

### Step 0: Initial Git Status Check

**[Mode: code]**

- Run `git status` to check current repository state
- Ensure working directory is clean or document existing changes
- **Success criteria:** Git status documented and ready for workflow

### Step 1: Current state validation

**[Mode: code]**

- Run `bun test` to establish baseline
- **Decision criteria:** If tests fail, fix issues before proceeding; if pass, continue
- **On failure:** Switch to [Mode: debug] to resolve existing test failures
- **Success criteria:** All existing tests pass

### Step 2: Dead code analysis

**[Mode: code]**

- Run `deno task check:module-export` to identify unused exports
- Document findings for API cleanup decisions
- **Prerequisites:** Test suite passes
- **On failure:** Switch to [Mode: debug] to resolve module analysis tool issues
- **Success criteria:** Dead code analysis report generated

### Step 3: API documentation review

**[Mode: ask]**

- Run `deno doc src/mod.ts` to generate current API documentation
- Analyze API from user perspective for usability issues
- **Prerequisites:** Module exports analysis completed
- **On failure:** Request manual API review if doc generation fails
- **Success criteria:** Current API structure documented and analyzed

### Step 4: API design analysis

**[Mode: architect]**

- Apply Hyrum's Law principles to identify breaking change risks
- Design improved API considering:
  - Backward compatibility where possible
  - Clear separation of concerns
  - Functional programming principles
  - Type safety improvements
- **Prerequisites:** API documentation and dead code analysis available
- **On failure:** Request stakeholder input on API design priorities
- **Success criteria:** New API design documented with migration strategy

### Step 5: Examples to specifications conversion

**[Mode: code]**

- Analyze existing `examples/*.ts` files to extract API usage patterns
- Convert example usage scenarios into comprehensive test specifications
- Create or update `spec/*.test.ts` files based on examples
- Ensure all API usage patterns from examples are covered in specifications
- **Prerequisites:** API design completed
- **On failure:** Switch to [Mode: debug] to resolve conversion issues
- **Success criteria:** All example usage patterns converted to test specifications

### Step 6: Specification updates

**[Mode: code]**

- Update or create additional `spec/*.test.ts` files for new API
- Update `src/types.ts` with new type definitions
- Ensure specifications cover all public API functions
- **Prerequisites:** Examples converted to specifications
- **On failure:** Switch to [Mode: debug] to resolve specification issues
- **Success criteria:** All API specifications compile and are comprehensive

### Step 7: Implementation updates

**[Mode: code]**

- Modify `src/*.ts` files to implement new API design
- Maintain backward compatibility where specified in design
- Follow functional domain modeling principles
- **Prerequisites:** Specifications updated and compiling
- **On failure:** Switch to [Mode: refactor] for complex implementation issues
- **Success criteria:** Implementation compiles without TypeScript errors

### Step 8: Incremental test validation

**[Mode: code]**

- Run tests after each major implementation change
- **Decision criteria:** If tests fail, fix immediately; if pass, continue implementation
- **Prerequisites:** Implementation changes applied
- **On failure:** Switch to [Mode: debug] to resolve test failures
- **Success criteria:** Tests pass after each implementation milestone

### Step 9: Final validation

**[Mode: code]**

- Run complete test suite: `bun test`
- Verify all specifications pass
- **Prerequisites:** All implementation completed
- **On failure:** Switch to [Mode: debug] for comprehensive failure analysis
- **Success criteria:** All tests pass, API refactoring complete

### Step 10: Final Git Commit

**[Mode: code]**

- Stage changes with `git add .`
- Commit with conventional commit message format:
  - `refactor!: redesign library API` for breaking changes
  - `feat!: improve API with breaking changes` for feature improvements with breaking changes
  - `refactor: improve API design` for non-breaking improvements
- **Prerequisites:** All tests pass and API refactoring complete
- **Success criteria:** Changes committed with appropriate conventional commit message indicating breaking changes if applicable
