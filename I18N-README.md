# i18n Translation Guide

Africa Climate Finance uses a dictionary-based translation system for **English (en)** and **Swahili (sw)**. The language dropdown in the header switches all visible text instantly.

## How It Works

- **Script**: `assets/js/i18n.js`
- **Storage**: `localStorage` key `climatefinance_lang`
- **URL override**: `?lang=en` or `?lang=sw` (overrides localStorage for that page)
- **Default**: English if nothing is set

## Adding New Translations

### 1. Add the key to `assets/js/i18n.js`

In the `TRANSLATIONS` object, add your key under both `en` and `sw`:

```javascript
en: {
  // ...
  mySection: {
    myKey: 'English text here',
  },
},
sw: {
  // ...
  mySection: {
    myKey: 'Maandishi ya Kiswahili hapa',
  },
},
```

### 2. Add the attribute to your HTML

| Use Case | Attribute | Example |
|----------|-----------|---------|
| Replace element text | `data-i18n="section.key"` | `<h1 data-i18n="team.title">Our Team</h1>` |
| Placeholder text | `data-i18n-placeholder="section.key"` | `<input data-i18n-placeholder="contact.namePlaceholder">` |
| Aria label | `data-i18n-aria="section.key"` | `<button data-i18n-aria="nav.searchAria">` |
| Title attribute | `data-i18n-title="section.key"` | `<abbr data-i18n-title="common.abbr">` |

### 3. Preserve icons inside links/buttons

Wrap only the translatable text in a `<span>` so the icon is not replaced:

```html
<a href="#" class="nav-link"><span data-i18n="nav.whatWeDo">What We Do</span> <i class="ri-add-line"></i></a>
```

## Key Naming Convention

- **Format**: `section.key` (dot-separated, camelCase for key)
- **Sections in use**: `nav`, `team`, `profile`, `cop`, `contact`, `footer`, `common`
- **Examples**: `nav.home`, `contact.sendMessage`, `profile.backToTeam`

## Testing

1. Open any page, click the language dropdown (Eng ▼), choose **Swahili**.
2. All `[data-i18n]` elements should update immediately.
3. Refresh the page - Swahili should persist.
4. Add `?lang=sw` to the URL - it overrides localStorage on load.
