# Security and Privacy Policy

## Supported Scope

This repository contains healthcare feature-engineering notebooks. Security and privacy reports should focus on:

- Accidental exposure of protected health information (PHI).
- Re-identification risk in sample data or derived features.
- Unsafe notebook outputs that reveal sensitive records.
- Dependency or notebook-execution risks.

## PHI Handling

Do not commit patient names, medical record numbers, phone numbers, addresses, exact dates of birth, raw hospital exports, or other direct identifiers. Use synthetic, public, anonymized, or approved teaching datasets.

Derived features can still be sensitive. Before committing notebook outputs or engineered features, confirm that small groups, rare diagnoses, or timestamp combinations do not make individuals re-identifiable.

## Reporting Sensitive Issues

Do not open a public issue containing PHI, credentials, or private dataset samples. Use GitHub private vulnerability reporting when available, or contact the maintainer through an approved private channel.

Include:

- A short description of the concern.
- The affected file or notebook.
- Whether sensitive data is present.
- Suggested remediation if known.
