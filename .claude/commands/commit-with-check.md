# Commit with check

Make sure all tests and lint checks pass before committing the current status to git.

## Command

```bash
# Test all
bun test

# Lint and type check all files
bun run lint

# commit
git commit -m "{message}"
```

## Success Metrics

- **Code quality:** Zero lint errors, all tests passing
- **Functionality:** All specified features working as intended
- **Maintainability:** Code follows functional programming principles
- **Type safety:** All functions use appropriate `Result<T, E>` types
- **Documentation:** API changes reflected in generated documentation

## Git Commit Message Conventions

All workflows follow conventional commit format:

- **feat:** A new feature
- **fix:** A bug fix
- **refactor:** A code change that neither fixes a bug nor adds a feature
- **docs:** Documentation only changes
- **test:** Adding missing tests or correcting existing tests
- **chore:** Changes to the build process or auxiliary tools
- **style:** Changes that do not affect the meaning of the code (formatting, etc.)

**Breaking Changes:** Add `!` after the type (e.g., `feat!:`, `refactor!:`) and include `BREAKING CHANGE:` in the commit body.

コミットメッセージは日本語で書いてください。
