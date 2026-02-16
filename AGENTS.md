# AGENTS.md - Control de Mercadería

## Project Overview

This is a Progressive Web App (PWA) for managing merchandise cuts and deliveries ("Control de Mercadería - Gestión de cortes y entregas"). Built with vanilla HTML/CSS/JS in a single `index.html` file.

## Build / Test Commands

### Running the Application

```bash
# Open index.html directly in browser
start index.html          # Windows
open index.html           # macOS
xdg-open index.html       # Linux
```

### Development Server (Optional)

```bash
# Using Python
python -m http.server 8000

# Using Node.js (if installed)
npx http-server -p 8000
```

Then open `http://localhost:8000` in your browser.

### Testing

- **No automated tests exist** - This is a vanilla JS project
- Manual testing: Open in browser, test all features (login, register, cortes, talleres, historial)
- Use browser DevTools (F12) for debugging

### Linting

- **No linting configured** - Consider adding ESLint if project grows

---

## Code Style Guidelines

### General Principles

- This is a vanilla HTML/CSS/JS project - no frameworks
- All code lives in `index.html` (CSS in `<style>`, JS in `<script>`)
- PWA with service worker in `service-worker.js`
- Uses ES5-compatible JavaScript (var declarations, function callbacks)

### HTML Style

```html
<!-- Use semantic HTML5 elements -->
<header>, <nav>, <main>, <section>, <div>

<!-- Attributes order: class, id, type, src, href, onclick, etc. -->
<input type="text" id="username" class="form-input" autocomplete="off">

<!-- Self-closing tags for void elements -->
<br>, <img>, <input>, <link>, <meta>
```

### CSS Style

```css
/* Use classes for styling, avoid inline styles */
.btn { padding: 14px; border-radius: 10px; }

/* Color scheme: Purple gradient primary (#667eea to #764ba2) */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Mobile-first, use flexbox/grid */
.app-container { display: flex; flex-direction: column; }

/* BEM-like naming for complex components */
.corte-item, .corte-header, .corte-colors
```

### JavaScript Style

```javascript
// Use var (ES5 compatible) - existing codebase pattern
var currentUser = null;
var users = [];

// Functions use function keyword, not arrow functions
function showLoginTab(tab, evt) { }

// Event handlers pass event object
function handleClick(event) { }

// DOM queries
document.getElementById('elementId');
document.querySelectorAll('.className');

// Use IIFE or inline event handlers (existing pattern)
// Avoid complex module systems

// Array methods with callbacks
users.find(function(u) { return u.usuario === username; });
cortes.filter(function(c) { return c.estado === 'pendiente'; });

// String concatenation for HTML (existing pattern)
html += '<div class="corte-item">' + name + '</div>';
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Functions | camelCase | `showLoginTab()`, `registrarCorte()` |
| Variables | camelCase | `currentUser`, `coloresCorte` |
| Constants | UPPER_SNAKE | `CACHE_NAME` (in service-worker.js) |
| CSS Classes | kebab-case | `.corte-item`, `.btn-primary` |
| IDs | camelCase | `loginSection`, `corteNombre` |
| Data Keys | camelCase | localStorage keys: `cortes`, `talleres` |

### Data Structures

```javascript
// User object
{ usuario: string, nombre: string, password: string }

// Corte object
{
    id: number,
    numCorte: number,
    nombre: string,
    colors: [{ color: string, nombre: string, cantidad: number, cantidadFinal: number }],
    multiplicador: number,
    total: number,
    estado: 'pendiente' | 'enviado' | 'retirado',
    taller: string | null,
    fechaEnvio: string | null,
    fechaRetiro: string | null,
    usuario: string,
    date: string
}

// Taller object
{ id: number, nombre: string, activo: boolean }

// Transaccion object
{ type: 'corte' | 'entrega' | 'retiro', numCorte, corteNombre, colors, ... }
```

### Error Handling

```javascript
// Use alert() for user-facing errors (existing pattern)
if (!nombre) { alert('Ingrese el nombre del corte'); return; }

// Use confirm() for destructive actions
if (!confirm('¿Está seguro de eliminar este corte?')) return;

// Console logging for debugging
console.log('verDetalle - transaccion:', transaccion);
```

### LocalStorage Usage

```javascript
// Save
localStorage.setItem('cortes', JSON.stringify(cortes));

// Load
var saved = localStorage.getItem('cortes');
if (saved) { cortes = JSON.parse(saved); }

// Keys: 'users', 'currentUser', 'cortes', 'talleres', 'transacciones'
```

### Service Worker (service-worker.js)

```javascript
const CACHE_NAME = 'mercaderia-v2';
var urlsToCache = ['./', './index.html', './manifest.json', ...];

self.addEventListener('install', function(event) { });
self.addEventListener('activate', function(event) { });
self.addEventListener('fetch', function(event) { });
```

### PWA Requirements

- Manifest: `manifest.json` with icons (192x192, 512x512)
- Service Worker: `service-worker.js` for offline capability
- Meta tags for mobile: theme-color, viewport, mobile-web-app-capable

---

## File Structure

```
aplicacion/
├── index.html          # Main app (HTML + CSS + JS)
├── manifest.json       # PWA manifest
├── service-worker.js   # PWA service worker
├── icon-192.png        # App icon 192px
├── icon-512.png        # App icon 512px
├── create_icons.py     # Script to generate icons
└── session-ses_*.md    # Session notes (ignore)
```

---

## Adding New Features

1. **UI Changes**: Edit HTML in `index.html`, add CSS in `<style>`
2. **Logic Changes**: Add JS functions in `<script>` at bottom of `index.html`
3. **PWA Updates**: Update `manifest.json` and `service-worker.js` CACHE_NAME

---

## Notes for Agents

- This is a Spanish-language application - all UI text is in Spanish
- No build process - changes are immediate on refresh
- Data persists in browser's localStorage
- Test in mobile view using DevTools for best experience
