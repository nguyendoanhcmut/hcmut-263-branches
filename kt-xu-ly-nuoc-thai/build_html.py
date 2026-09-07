import os
import sys

md_path = r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai\indexes\test_branches_deep\wastewater_treatment_deep_branches.md"
html_path = r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai\indexes\test_branches_deep\wastewater_treatment_deep_branches.html"

print(f"Reading markdown from: {md_path}")
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

print(f"Markdown read: {len(md_content)} chars, {len(md_content.encode('utf-8'))} bytes")

# Ensure no </script> tag breaks the template
if "</script>" in md_content.lower():
    print("Escaping </script> tags...")
    md_content = md_content.replace("</script>", "<\\/script>")

frontmatter = """---
markmap:
  initialExpandLevel: 2
  maxWidth: 420
---
"""

html_header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>K\u1ef9 thu\u1eadt X\u1eed l\u00fd N\u01b0\u1edbc th\u1ea3i (Wastewater Treatment Engineering) - Deep Tree</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script>
    (function() {
      try {
        const stored = localStorage.getItem('markmap-theme');
        const theme = (stored === 'dark' || stored === 'light') ? stored : (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', theme);
        if (theme === 'dark') {
          document.documentElement.classList.add('dark', 'markmap-dark');
        } else {
          document.documentElement.classList.remove('dark', 'markmap-dark');
        }
      } catch (e) {}
    })();
  </script>
  <style>
    :root {
      --bg-primary: #fafbfc;
      --card-bg: rgba(255, 255, 255, 0.95);
      --border-color: #e2e8f0;
      --text-primary: #0f172a;
      --hint-text: #64748b;
      --btn-bg: #ffffff;
      --btn-border: #cbd5e1;
      --btn-text: #334155;
      --btn-hover-bg: #f8fafc;
      --btn-hover-border: #94a3b8;
      --btn-hover-text: #0f172a;
      --shadow: 0 2px 8px rgba(0, 0, 0, 0.08);

      --markmap-text-color: #0f172a;
      --markmap-circle-open-bg: #ffffff;
      --markmap-code-bg: #f1f5f9;
      --markmap-code-color: #0f172a;
      --markmap-a-color: #0369a1;
      --markmap-a-hover-color: #0284c7;
    }

    [data-theme="dark"],
    .dark,
    .markmap-dark {
      --bg-primary: #0b0f19;
      --card-bg: rgba(15, 23, 42, 0.95);
      --border-color: #334155;
      --text-primary: #f8fafc;
      --hint-text: #94a3b8;
      --btn-bg: #1e293b;
      --btn-border: #475569;
      --btn-text: #e2e8f0;
      --btn-hover-bg: #334155;
      --btn-hover-border: #64748b;
      --btn-hover-text: #ffffff;
      --shadow: 0 2px 8px rgba(0, 0, 0, 0.4);

      --markmap-text-color: #f8fafc;
      --markmap-circle-open-bg: #0b0f19;
      --markmap-code-bg: #1e293b;
      --markmap-code-color: #f8fafc;
      --markmap-a-color: #38bdf8;
      --markmap-a-hover-color: #7dd3fc;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    html, body {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      transition: background-color 0.25s ease, color 0.25s ease;
    }
    .markmap {
      width: 100vw;
      height: 100vh;
      position: relative;
    }
    .markmap > svg {
      width: 100%;
      height: 100%;
      display: block;
    }
    .markmap, .markmap .katex {
      color: var(--markmap-text-color);
    }
    .toolbar {
      position: fixed;
      top: 16px;
      right: 16px;
      display: flex;
      gap: 8px;
      z-index: 100;
      background: var(--card-bg);
      padding: 6px;
      border-radius: 8px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border-color);
      transition: background-color 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }
    .toolbar button {
      border: 1px solid var(--btn-border);
      background: var(--btn-bg);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
      font-weight: 500;
      color: var(--btn-text);
      font-family: inherit;
      transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
    }
    .toolbar button:hover {
      background: var(--btn-hover-bg);
      border-color: var(--btn-hover-border);
      color: var(--btn-hover-text);
    }
    #theme-toggle {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 9px;
    }
    #theme-toggle svg {
      width: 15px;
      height: 15px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      display: block;
    }
    #theme-toggle .icon-sun {
      display: none;
    }
    #theme-toggle .icon-moon {
      display: block;
    }
    [data-theme="dark"] #theme-toggle .icon-sun,
    .dark #theme-toggle .icon-sun,
    .markmap-dark #theme-toggle .icon-sun {
      display: block;
    }
    [data-theme="dark"] #theme-toggle .icon-moon,
    .dark #theme-toggle .icon-moon,
    .markmap-dark #theme-toggle .icon-moon {
      display: none;
    }
    .title-bar {
      position: fixed;
      bottom: 16px;
      left: 16px;
      z-index: 100;
      background: var(--card-bg);
      padding: 10px 16px;
      border-radius: 8px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border-color);
      pointer-events: none;
      transition: background-color 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }
    .title-bar h1 {
      font-size: 15px;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 3px;
      transition: color 0.25s ease;
    }
    .title-bar p {
      font-size: 12px;
      color: var(--hint-text);
      transition: color 0.25s ease;
    }
  </style>
</head>
<body>

  <div class="toolbar">
    <button onclick="if(window.mm) window.mm.fit()">Fit</button>
    <button onclick="if(window.mm) window.mm.rescale(1.25)">Zoom In (+)</button>
    <button onclick="if(window.mm) window.mm.rescale(0.8)">Zoom Out (-)</button>
    <button id="theme-toggle" aria-label="Toggle theme" title="Toggle theme" onclick="window.__toggleTheme && window.__toggleTheme()">
      <svg class="icon-moon" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
      </svg>
      <svg class="icon-sun" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="5"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
    </button>
  </div>

  <div class="title-bar">
    <h1 id="doc-title">K\u1ef9 thu\u1eadt X\u1eed l\u00fd N\u01b0\u1edbc th\u1ea3i (Wastewater Treatment Engineering) - Deep Tree</h1>
    <p>Scroll to zoom \u00b7 Drag to pan \u00b7 Click circles to expand / collapse deep branches</p>
  </div>

  <div class="markmap">
    <script type="text/template">
"""

html_footer = """
    </script>
  </div>

  <script>
    const lightPalette = ['#0369a1', '#c2410c', '#15803d', '#b91c1c', '#7e22ce', '#be185d', '#0f766e', '#a16207', '#6d28d9', '#047857'];
    const darkPalette = ['#38bdf8', '#fb923c', '#4ade80', '#f87171', '#c084fc', '#f472b6', '#2dd4bf', '#facc15', '#a78bfa', '#34d399'];

    function createColorFunction(theme) {
      const palette = theme === 'dark' ? darkPalette : lightPalette;
      const ordinal = (window.d3 && window.d3.scaleOrdinal) ? window.d3.scaleOrdinal(palette) : null;
      return function(node) {
        const p = typeof node === 'string' ? node : `${(node && node.state && node.state.path) || ''}`;
        if (ordinal) {
          return ordinal(p);
        }
        let h = 0;
        for (let i = 0; i < p.length; i++) {
          h = ((h << 5) - h) + p.charCodeAt(i);
          h |= 0;
        }
        return palette[Math.abs(h) % palette.length];
      };
    }

    function applyTheme(theme, persist) {
      document.documentElement.setAttribute('data-theme', theme);
      if (theme === 'dark') {
        document.documentElement.classList.add('dark', 'markmap-dark');
      } else {
        document.documentElement.classList.remove('dark', 'markmap-dark');
      }
      if (persist) {
        try {
          localStorage.setItem('markmap-theme', theme);
        } catch (e) {}
      }
      if (window.mm) {
        const colorFn = createColorFunction(theme);
        window.mm.setOptions({
          color: (node) => colorFn(node)
        });
        window.mm.renderData();
      }
    }

    window.__toggleTheme = function() {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next, true);
    };

    try {
      if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
          if (!localStorage.getItem('markmap-theme')) {
            applyTheme(e.matches ? 'dark' : 'light', false);
          }
        });
      }
    } catch (e) {}

    window.markmap = {
      autoLoader: {
        toolbar: false,
        onReady() {
          const origCreate = window.markmap.Markmap.create;
          window.markmap.Markmap.create = function(svg, opts, data) {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
            const colorFn = createColorFunction(currentTheme);
            const customOpts = {
              ...opts,
              color: (node) => colorFn(node)
            };
            const instance = origCreate.call(this, svg, customOpts, data);
            window.mm = instance;
            return instance;
          };
        }
      }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@0.18"></script>
</body>
</html>
"""

print(f"Writing complete HTML to: {html_path}")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_header)
    f.write(frontmatter)
    f.write(md_content)
    f.write(html_footer)

size = os.path.getsize(html_path)
print(f"HTML generated successfully: {size} bytes ({size / (1024*1024):.2f} MB)")
