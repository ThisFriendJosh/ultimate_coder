# Ultimate Coder

A 26‑week, weekly‑sprint program to level up from Novice → Principal by **learning through building**.

**Cadence:** weekly_sprints · **Duration:** 26 weeks · **Hours/week:** 12–20

## Tracks
- CS Fundamentals (`tracks/cs`)
- Language Mastery (`tracks/langs`)
- Systems & Architecture (`tracks/systems`)
- DevOps (`tracks/devops`)
- Data & AI (`tracks/data_ai`)

## Sprint Rhythm
- **d1: plan** → scope, acceptances, risks
- **d2–3: build** → implement, tests
- **d4: harden** → perf, security, docs
- **d5: review** → demo, retro, next sprint

## Artifacts
- Portfolio repo, tech notes, and 3 showcase projects
- CI/CD and typed + tested code
- Threat model + fixes

See `docs/syllabus.md` and `ultimate_coder.yaml` for the canonical program spec.

## Scripts

The repository includes helper scripts under `scripts/`.

### `uc-open-pr.sh`

Creates a branch, copies a file into the repo, commits, pushes, and (if the `gh` CLI is installed) opens a pull request.

```bash
scripts/uc-open-pr.sh <branch-name> <source-file> <commit-message> [destination]
```

The optional `destination` argument controls where the file is copied inside the repository (defaults to the basename of the source file).
