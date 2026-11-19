---
hide:
  - navigation
---

# Calydon: High-Level Design Document

| Item | Detail |
|---|---|
| **Game** | *Calydon*, an action-adventure RPG |
| **Document** | High-Level Design Document |
| **Version** | 3.0 (redacted for portfolio use) |
| **Author** | Richard Rabil, Jr. |
| **Engine** | BioWare's Neverwinter Nights™ Aurora Toolset |
| **Platform** | Windows / PC |

*Calydon* is an RPG set in the fictional city of Romera, where a new body of believers called the Calydonians have sparked a mass conversion and growing religious strife. The Emperor enlists Brynn Harrowmage, a dangerous prisoner of war, to assassinate the Calydonians' leader in exchange for freedom for Brynn and his captive sister.

This design document lays the conceptual foundation for the game: its world, characters, story structure, interface, levels, gameplay, art, and audio.

!!! info "Redacted version"

    Parts of this document are marked <span class="redacted">Redacted</span>. Those passages were removed from the original before it was shared as a writing sample.

## Contents

| Section | What it covers |
|---|---|
| [1. Calydon Quick Sheet](01-quick-sheet.md) | The big idea, genre, platform, audience, and key selling points at a glance |
| [2. Product Overview](02-product-overview.md) | The setting, premise, and the player's mission |
| [3. Purpose and Organization](03-purpose-and-organization.md) | Why this document exists and how it is organized |
| [4. Opening Gameplay ("The Grabber")](04-opening-gameplay.md) | The opening scene that hooks the player |
| [5. Races, Characters, Factions, and Nationalities](05-races-characters-factions.md) | Who the player meets and the groups they belong to |
| [6. Story Structure](06-story-structure.md) | The seven parts of the story, with activity diagrams |
| [7. Interface](07-interface.md) | The radial menu, main gameplay screen, and panels |
| [8. Obstacles](08-obstacles.md) | Enemies and puzzles |
| [9. Level Walkthrough](09-level-walkthrough.md) | The game's major areas, in the order the player reaches them |
| [10. Gameplay](10-gameplay.md) | Controls, character actions, exploration, and effects on the character |
| [11. Art](11-art.md) | Concepts for characters, items, and the world |
| [12. Audio Requirements](12-audio-requirements.md) | Character sounds, enemy sounds, music, and voice recording |

## About this edition

I wrote this document in 2011 as a Word file. This web edition, made in 2026, presents it the way a design team would keep a living spec: as plain Markdown files in a Git repository, built into a website by [MkDocs](https://www.mkdocs.org/) with the [Material](https://squidfunk.github.io/mkdocs-material/) theme, and published automatically by GitHub Pages each time a change is saved. The text is unchanged apart from light formatting fixes. The story diagrams in Section 6 are now written as text with [Mermaid](https://mermaid.js.org/), so they can be edited like the rest of the document.
