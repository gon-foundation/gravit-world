# gravit.world

Website of the **Gravit Open Network Foundation** (Verein nach Schweizer Recht, Zürich),
in German, French, Italian and English. German is the legally authoritative language;
the Impressum exists only in DE / FR / IT.

- `src/content/site.py` — all texts, people, news; `PENDING(...)` blocks production.
- `src/content/statuten_de.json` — statutes, exported from the Foundation's legal package.
- `build.py` — static site generator (standard library only).

Merging to `main` publishes to **gravit.world/preview/**. The live site is updated only by
running the *Site* workflow manually with target `production`.
