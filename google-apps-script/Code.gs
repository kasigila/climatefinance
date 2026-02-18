/**
 * Africa Climate Finance - Form Handler
 * Deploy as Web App: Execute as Me, Who has access: Anyone
 * Method: POST | Forms submit name, email, phone?, msg_subject?, message, _formType?
 */

// === CONFIGURE THESE ===
const RECIPIENT_EMAIL = '';  // Your email to receive submissions (e.g. 'you@example.com')
const SITE_URL = 'https://kasigila.github.io/climatefinance/';
const SUBMISSIONS_SHEET_ID = '1wFy-f1Aw0DPyfeSxA5Dq_y3lvZ6ZG4kLujAUsW7WjTI';  // africa-climate-finance

// Brand colors (match assets/css/style.css)
const BRAND_GREEN = '#40865b';
const BRAND_GREEN_DARK = '#265037';
const TEXT_DARK = '#333333';
const TEXT_MUTED = '#666666';
const LOGO_URL = SITE_URL + 'assets/img/logo.png';

/**
 * Handle form POST submissions
 */
function doPost(e) {
  try {
    const p = e?.parameter || {};
    const formType = p._formType || (p._subject && String(p._subject).indexOf('Event') >= 0 ? 'event' : 'contact');

    const submission = {
      name: p.name || '',
      email: p.email || '',
      phone: p.phone || p.phone_number || '',
      subject: p.msg_subject || p._subject || 'Form Submission',
      message: p.message || ''
    };

    if (!RECIPIENT_EMAIL) {
      return createResponse(false, 'Server not configured. Set RECIPIENT_EMAIL in Code.gs');
    }

    const ownerHtml = buildOwnerEmail(submission, formType);
    const confirmHtml = buildConfirmationEmail(submission, formType);

    GmailApp.sendEmail(RECIPIENT_EMAIL, '[Africa Climate Finance] ' + submission.subject, '', {
      htmlBody: ownerHtml,
      replyTo: submission.email || undefined
    });

    if (submission.email && confirmHtml) {
      GmailApp.sendEmail(submission.email, 'Thank you for contacting Africa Climate Finance', '', {
        htmlBody: confirmHtml,
        name: 'Africa Climate Finance'
      });
    }

    if (SUBMISSIONS_SHEET_ID) {
      logToSheet(submission, formType);
    }

    return createThankYouPage(submission, formType);
  } catch (err) {
    Logger.log(err);
    return createResponse(false, err.toString());
  }
}

/**
 * Handle GET (redirect to site or show instructions)
 */
function doGet(e) {
  return HtmlService.createHtmlOutput(
    '<p style="font-family:sans-serif;">Form handler is active. Submit via POST from your contact form.</p>' +
    '<p><a href="' + SITE_URL + '">Back to Africa Climate Finance</a></p>'
  ).setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function createResponse(success, message) {
  const mimeType = ContentService.MimeType.JSON;
  const output = ContentService.createTextOutput(JSON.stringify({ success, message })).setMimeType(mimeType);
  return output;
}

/**
 * Full HTML thank-you page returned after form POST (when using form action)
 */
function createThankYouPage(submission, formType) {
  const html = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;600;700&family=Spline+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <title>Thank You - Africa Climate Finance</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Spline Sans', sans-serif; background: #f5f5f5; color: ${TEXT_DARK}; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem; }
    .card { max-width: 480px; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 24px rgba(0,0,0,.08); }
    .header { background: ${BRAND_GREEN}; color: #fff; padding: 2rem; text-align: center; }
    .header h1 { font-family: 'Readex Pro', sans-serif; font-size: 1.5rem; font-weight: 700; margin-bottom: .5rem; }
    .header p { opacity: .9; font-size: .95rem; }
    .body { padding: 2rem; }
    .body p { line-height: 1.7; color: ${TEXT_MUTED}; margin-bottom: 1rem; }
    .btn { display: inline-block; background: ${BRAND_GREEN}; color: #fff !important; padding: .75rem 1.5rem; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: .95rem; margin-top: .5rem; transition: background .2s; }
    .btn:hover { background: ${BRAND_GREEN_DARK}; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h1>Message Received</h1>
      <p>Africa Climate Finance</p>
    </div>
    <div class="body">
      <p>Thank you, ${escapeHtml(submission.name) || 'there'}! We have received your message and will get back to you soon.</p>
      <p>We sent a confirmation to ${escapeHtml(submission.email) || 'your email'}.</p>
      <a href="${SITE_URL}" class="btn">Return to Website</a>
    </div>
  </div>
</body>
</html>`;
  return HtmlService.createHtmlOutput(html).setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function buildOwnerEmail(sub, formType) {
  const isEvent = formType === 'event';
  const title = isEvent ? 'Event Registration' : 'New Contact Form Submission';
  return `
<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;600;700&family=Spline+Sans:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body style="margin:0;font-family:'Spline Sans',Arial,sans-serif;background:#fff;color:${TEXT_DARK};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;">
    <tr>
      <td style="padding:32px 24px 24px;border-bottom:2px solid ${BRAND_GREEN};text-align:center;background:#fff;">
        <a href="${SITE_URL}" style="text-decoration:none;"><img src="${LOGO_URL}" alt="Africa Climate Finance" width="180" height="auto" style="display:block;margin:0 auto;max-width:180px;"></a>
        <p style="margin:12px 0 0;font-family:'Readex Pro',sans-serif;font-size:11px;color:${TEXT_MUTED};letter-spacing:0.5px;">TANZANIA &amp; BEYOND</p>
      </td>
    </tr>
    <tr>
      <td style="padding:28px 24px;">
        <p style="margin:0 0 20px;font-size:13px;color:${TEXT_MUTED};text-transform:uppercase;letter-spacing:1px;">${escapeHtml(title)}</p>
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;font-size:15px;">
          <tr><td style="padding:12px 0;border-bottom:1px solid #eee;"><strong style="color:${TEXT_MUTED};font-weight:500;">Name</strong></td><td style="padding:12px 0;border-bottom:1px solid #eee;">${escapeHtml(sub.name)}</td></tr>
          <tr><td style="padding:12px 0;border-bottom:1px solid #eee;"><strong style="color:${TEXT_MUTED};font-weight:500;">Email</strong></td><td style="padding:12px 0;border-bottom:1px solid #eee;">${escapeHtml(sub.email)}</td></tr>
          ${sub.phone ? `<tr><td style="padding:12px 0;border-bottom:1px solid #eee;"><strong style="color:${TEXT_MUTED};font-weight:500;">Phone</strong></td><td style="padding:12px 0;border-bottom:1px solid #eee;">${escapeHtml(sub.phone)}</td></tr>` : ''}
          ${sub.subject ? `<tr><td style="padding:12px 0;border-bottom:1px solid #eee;"><strong style="color:${TEXT_MUTED};font-weight:500;">Subject</strong></td><td style="padding:12px 0;border-bottom:1px solid #eee;">${escapeHtml(sub.subject)}</td></tr>` : ''}
        </table>
        ${sub.message ? `<div style="margin-top:24px;padding-top:20px;border-top:1px solid #eee;"><strong style="color:${TEXT_MUTED};font-weight:500;font-size:13px;">Message</strong><p style="margin:12px 0 0;line-height:1.6;color:${TEXT_DARK};white-space:pre-wrap;">${escapeHtml(sub.message)}</p></div>` : ''}
        <p style="margin:28px 0 0;font-size:12px;color:${TEXT_MUTED};">Submitted via <a href="${SITE_URL}" style="color:${BRAND_GREEN};text-decoration:none;">Africa Climate Finance</a></p>
      </td>
    </tr>
    <tr>
      <td style="padding:16px 24px;background:#f9f9f9;font-size:11px;color:${TEXT_MUTED};">
        Africa Climate Finance &middot; Masaki, Dar es Salaam &middot; P.O. Box 6756
      </td>
    </tr>
  </table>
</body>
</html>`;
}

function buildConfirmationEmail(sub, formType) {
  const isEvent = formType === 'event';
  const intro = isEvent
    ? 'Thank you for registering your interest in our event. We will be in touch shortly with further details.'
    : 'Thank you for contacting Africa Climate Finance. We have received your message and will respond within 1–2 business days.';
  return `
<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;600;700&family=Spline+Sans:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body style="margin:0;font-family:'Spline Sans',Arial,sans-serif;background:#fff;color:${TEXT_DARK};">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;">
    <tr>
      <td style="padding:32px 24px 24px;border-bottom:2px solid ${BRAND_GREEN};text-align:center;background:#fff;">
        <a href="${SITE_URL}" style="text-decoration:none;"><img src="${LOGO_URL}" alt="Africa Climate Finance" width="180" height="auto" style="display:block;margin:0 auto;max-width:180px;"></a>
        <p style="margin:12px 0 0;font-family:'Readex Pro',sans-serif;font-size:11px;color:${TEXT_MUTED};letter-spacing:0.5px;">TANZANIA &amp; BEYOND</p>
      </td>
    </tr>
    <tr>
      <td style="padding:32px 24px;">
        <p style="margin:0 0 20px;font-size:16px;color:${TEXT_DARK};font-weight:500;">Dear ${escapeHtml(sub.name) || 'Valued Contact'},</p>
        <p style="margin:0 0 24px;line-height:1.7;color:${TEXT_DARK};font-size:15px;">${intro}</p>
        <p style="margin:0 0 28px;line-height:1.7;color:${TEXT_DARK};font-size:15px;">Best regards,</p>
        <p style="margin:0 0 24px;font-weight:600;color:${TEXT_DARK};font-size:15px;">The Africa Climate Finance Team</p>
        <a href="${SITE_URL}" style="display:inline-block;background:${BRAND_GREEN};color:#fff;padding:12px 24px;text-decoration:none;font-weight:600;font-size:14px;">Visit Our Website</a>
      </td>
    </tr>
    <tr>
      <td style="padding:16px 24px;background:#f9f9f9;font-size:11px;color:${TEXT_MUTED};">
        Africa Climate Finance &middot; Masaki, Dar es Salaam &middot; P.O. Box 6756
      </td>
    </tr>
  </table>
</body>
</html>`;
}

function escapeHtml(str) {
  if (!str || typeof str !== 'string') return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/**
 * Append submission to a Google Sheet for tracking.
 * Create a sheet, copy its ID from the URL, paste into SUBMISSIONS_SHEET_ID.
 * Run setupSubmissionsSheet() once to add headers (or add them manually).
 */
function logToSheet(submission, formType) {
  try {
    const sheet = SpreadsheetApp.openById(SUBMISSIONS_SHEET_ID).getSheets()[0];
    const hasHeaders = sheet.getLastRow() >= 1;
    if (!hasHeaders) {
      sheet.getRange(1, 1, 1, 7).setValues([['Timestamp', 'Form Type', 'Name', 'Email', 'Phone', 'Subject', 'Message']]);
      sheet.getRange(1, 1, 1, 7).setFontWeight('bold');
    }
    sheet.appendRow([
      new Date(),
      formType,
      submission.name || '',
      submission.email || '',
      submission.phone || '',
      submission.subject || '',
      (submission.message || '').replace(/\r\n/g, '\n')
    ]);
  } catch (err) {
    Logger.log('logToSheet error: ' + err);
  }
}

/**
 * Run this once from the Apps Script editor (Run > setupSubmissionsSheet) to add headers to your sheet.
 */
function setupSubmissionsSheet() {
  if (!SUBMISSIONS_SHEET_ID) {
    Logger.log('Set SUBMISSIONS_SHEET_ID in Code.gs first, then run this.');
    return;
  }
  const sheet = SpreadsheetApp.openById(SUBMISSIONS_SHEET_ID).getSheets()[0];
  if (sheet.getLastRow() === 0) {
    sheet.getRange(1, 1, 1, 7).setValues([['Timestamp', 'Form Type', 'Name', 'Email', 'Phone', 'Subject', 'Message']]);
    sheet.getRange(1, 1, 1, 7).setFontWeight('bold');
    Logger.log('Headers added.');
  } else {
    Logger.log('Sheet already has data. Headers may exist.');
  }
}
