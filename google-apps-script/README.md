# Google Apps Script – Form Handler Setup

This script replaces Formspree and handles form submissions from your Africa Climate Finance site. It sends styled HTML emails that match your site’s look and sends confirmation emails to submitters.

## Setup

### 1. Create the script

1. Go to [script.google.com](https://script.google.com)
2. Click **New project**
3. Delete any default code
4. Copy everything from `Code.gs` into the editor
5. Set `RECIPIENT_EMAIL` to your email
6. Set `SITE_URL` if different (default: `https://kasigila.github.io/climatefinance/`)
7. Optionally set `SUBMISSIONS_SHEET_ID` for Google Sheets tracking (see below)
8. Save (Ctrl/Cmd + S)

### 2. Deploy as Web App

1. Click **Deploy** → **New deployment**
2. Click the gear icon next to **Select type** → choose **Web app**
3. Settings:
   - **Description:** Form handler (optional)
   - **Execute as:** Me
   - **Who has access:** Anyone
4. Click **Deploy**
5. Copy the **Web app URL** (e.g. `https://script.google.com/macros/s/.../exec`)

### 3. Connect your site

1. Open `assets/js/form-config.js` in your repo
2. Replace `YOUR_GOOGLE_APPS_SCRIPT_WEB_APP_URL` with your Web app URL:

   ```js
   window.FORM_ACTION_URL = 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec';
   ```

3. Deploy your site (push to GitHub if using GitHub Pages)

### 4. First run

1. Visit your site and submit the contact form
2. Approve access when Google asks (first request only)
3. Check your inbox for the styled submission email

## Behavior

- **Contact form** (`contact.php.html`): Sends you the full message; sends a confirmation to the visitor
- **Event registration** (`event-details.html`): Same flow, with an “Event Registration” email type

All emails use your brand colors (#40865b, #265037) and fonts (Readex Pro, Spline Sans).

## Tracking submissions in Google Sheets

1. Create a new Google Sheet (or use an existing one)
2. Copy the Sheet ID from the URL: `https://docs.google.com/spreadsheets/d/**SHEET_ID_HERE**/edit`
3. Paste it into `SUBMISSIONS_SHEET_ID` in Code.gs
4. Run **setupSubmissionsSheet** once: in the script editor, select it from the function dropdown, click Run
5. Redeploy the Web app

Each submission is appended as a new row: Timestamp | Form Type | Name | Email | Phone | Subject | Message. Leave `SUBMISSIONS_SHEET_ID` empty if you don’t need tracking.

## Troubleshooting

- **Form not submitting:** Ensure `FORM_ACTION_URL` in `form-config.js` starts with `http` and points to your deployed script
- **No emails:** Check that `RECIPIENT_EMAIL` is set in Code.gs and that you approved access on first run
- **CORS / security:** Using form `action` with a normal POST avoids CORS; the user is redirected to a thank-you page
