# Event Video Pros website

Static site, no build step. This folder IS the git repo root; it deploys to
GitHub Pages on every push to `main`.

## Repo (created under the org — do not use a Downstage-Systems URL)

    https://github.com/R3MediaPro/EventVideoPros-Website

R3-family repos live in the **R3MediaPro** organization. Downstage Systems
repos stayed on the personal `Downstage-Systems` account. To fix a stale
remote:

    git remote set-url origin https://github.com/R3MediaPro/EventVideoPros-Website.git

## Deploying

    git add -A && git commit -m "..." && git push

Live at https://eventvideopros.com. `CNAME` holds the custom domain — never
delete it.

## Brand

EVP is the corporate-event brand, a division of R3 Media Production
(https://r3mediapro.com). Deliberately a **light** theme, in contrast to R3's
dark one.

- Slate blue `#4C5A99` — the logo colour, drives buttons and links
- Gold `#C19A36` — accent for eyebrow/kicker text and the CTA-band hairline
- Charcoal `#2E2E2E` body text on white / `#F8F9FA`
- The style guide's electric blue `#1E90FF` was **dropped on purpose** — too
  generic. Don't reintroduce it.
- Logo lockup: `assets/evp-mark.png` + "Event Video Pros" text

Source brand assets (logos, client logos, style guide PDFs) are one folder up,
outside the repo.

## Positioning (matters for SEO)

EVP targets **national** corporate/conference video; R3 targets **Denver-local**.
Keeping them distinct stops the two sites competing for the same keywords. EVP
mentions Colorado as its base but should not be rewritten as a local-Denver site.

## House style

Plain sentences. **Avoid em dashes and standalone hyphens** as connectors —
use commas, colons, or two sentences. Hyphens are fine inside real compounds
(multi-camera, agency-level).

## Notes

- Contact form posts to Formspree `meeyyjpn`, shared with the R3 site; a hidden
  `brand=Event Video Pros` field distinguishes the leads.
- EVP has its own client portal at `portal/event.html`. It is **one file
  shared with the R3 site**, not a copy: the page skins itself from the domain
  it is served from, light slate and gold here, dark red on r3mediapro.com.
  The source of truth lives in the R3 website repo at `site/portal/event.html`
  and `deploy.sh` in the Video Editing Tracker folder copies it here on every
  deploy, so the two can never drift. Edit it there, never here.
  Which brand a client gets is set per project in the tracker, under
  Sync, "Delivered as", which decides the domain their link points at.
- Domains coloradoeventvideo.com, eventvideographernearme.com and
  eventvideoservices.com are meant to 301-redirect here.
