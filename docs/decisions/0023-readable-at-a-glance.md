# 0023. Readable at a glance

Status: accepted, 2026-11-03

## Context

The user said "it is imperative that anything played back is in clear human readable form" and "any document or message that is for human consumption needs to be optimized for human readability."

## Decision

Every document and message meant for a person follows these rules: one decision per question; one question at a time, the next waiting for the answer; a question gives the reader enough to answer without asking back, a concrete example of each option in the project's own terms and what each costs, and process notes aren't supporting detail; a short title; at most two short background sentences; two or three one-line options; short bullets under `## ` subheads with a blank line around each subhead; no walls of text. The framework carries its own copy of these rules; where it keeps them is decided at Behaviour and Design.
