WELCOME BEATRICE — iMESSAGE RICH PREVIEW TEST

FILES
- index-square.html: Uses the 1200 × 1200 cover preview.
- index-wide.html: Uses the 1200 × 630 cover preview.
- preview-only-square.html: Safer public test page without the baby photo.
- preview-only-wide.html: Safer public test page without the baby photo.
- welcome-beatrice-og-square.jpg
- welcome-beatrice-og-wide.jpg
- apple-touch-icon.png
- beatrice_card_photo.jpg
- configure_base_url.py

SETUP
1. Upload this folder to a publicly reachable HTTPS location.
2. In a terminal inside the folder, run:
   python configure_base_url.py https://YOUR-PUBLIC-HOST/PATH
3. Confirm that each URL opens without authentication:
   https://YOUR-PUBLIC-HOST/PATH/index-square.html
   https://YOUR-PUBLIC-HOST/PATH/index-wide.html
   https://YOUR-PUBLIC-HOST/PATH/welcome-beatrice-og-square.jpg
   https://YOUR-PUBLIC-HOST/PATH/welcome-beatrice-og-wide.jpg
4. Send each HTML URL as its own iMessage to compare the previews.
5. If Messages shows an older cached preview, use a new page URL or append
   a version query such as ?v=2.

IMPORTANT
- A local file:// URL will not generate the preview on another iPhone.
- Open Graph metadata must be present directly in the HTML head.
- The preview image URL must be an absolute public HTTPS URL.
- Publishing the full page also publishes the baby photo, name, and birth date
  to anyone who has the link and to preview crawlers.
