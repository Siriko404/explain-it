# Install

Two files to copy. Restart Claude Code.

## macOS / Linux

```bash
git clone https://github.com/Siriko404/explain-it.git
cd explain-it

cp -r skills/explain-it ~/.claude/skills/
cp commands/explain-it.md ~/.claude/commands/
cp commands/explain-it-now.md ~/.claude/commands/
```

## Windows (PowerShell)

```powershell
git clone https://github.com/Siriko404/explain-it.git
Set-Location explain-it

Copy-Item -Recurse skills/explain-it $env:USERPROFILE/.claude/skills/
Copy-Item commands/explain-it.md $env:USERPROFILE/.claude/commands/
Copy-Item commands/explain-it-now.md $env:USERPROFILE/.claude/commands/
```

## Upgrading from v1.x (`teacher-mode`)

v1.x shipped as `~/.claude/skills/teacher-mode/`. v2 ships as `~/.claude/skills/explain-it/`. The two are independent — remove v1.x first to avoid confusion:

```bash
rm -rf ~/.claude/skills/teacher-mode    # macOS / Linux
```

```powershell
Remove-Item -Recurse -Force $env:USERPROFILE/.claude/skills/teacher-mode    # Windows
```

Then run the install steps above.

## Verify install

In a fresh Claude Code conversation:

```
/explain-it difference-in-differences
```

Expected behavior:

1. Claude asks the seed question (*"What part of difference-in-differences do you understand least right now — A: definition, B: mechanics, C: when to use, D: other?"*)
2. After your answer, Claude emits a 3-node plan tree
3. Claude fires the plan-approval gate via `AskUserQuestion`
4. On approval, Claude walks the tree one node per chunk, big-picture first, with a visual element each, firing an `AskUserQuestion` stop-and-check gate after each chunk with 4 chunk-tailored options: Yes (Recommended) / No — `<predicted-confusion>` / Branch deeper — `<predicted-focus>` / Other

If any of these phases is skipped, the skill is not installed correctly — re-check the file paths above.

## Uninstall

```bash
rm -rf ~/.claude/skills/explain-it
rm ~/.claude/commands/explain-it.md
rm ~/.claude/commands/explain-it-now.md
```

## Update

```bash
cd explain-it
git pull
# Re-copy the files (same commands as install above)
```

## Plugin packaging (v2.1)

A `.claude-plugin` manifest for one-command install is planned for v2.1. Until then, manual copy is the supported install path.
