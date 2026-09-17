const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3001;

function getBriefHtml() {
  const briefPath = path.join(__dirname, 'public', 'index.html');
  try {
    return fs.readFileSync(briefPath, 'utf8');
  } catch (e) {
    return '<h1>Error loading Reservoir Launch Brief</h1>';
  }
}

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.json': 'application/json',
  '.mp4': 'video/mp4'
};

const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsedUrl.pathname;

  // Health check endpoint
  if (pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', site: 'reservoir-brief' }));
    return;
  }

  // Serve static files from public directory if exists (e.g. /launch_video_1979.png)
  if (pathname !== '/' && pathname !== '') {
    const filePath = path.join(__dirname, 'public', pathname);
    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': contentType, 'cache-control': 'public, max-age=86400' });
      fs.createReadStream(filePath).pipe(res);
      return;
    }
  }

  // All GET requests serve the brief directly with no password required
  if (req.method === 'GET' || req.method === 'HEAD') {
    res.writeHead(200, {
      'Content-Type': 'text/html; charset=utf-8',
      'cache-control': 'no-cache'
    });
    res.end(getBriefHtml());
    return;
  }

  // Fallback
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('OK');
});

server.listen(PORT, () => {
  console.log(`Reservoir Launch Brief running at http://localhost:${PORT}`);
  console.log(`Password protection: DISABLED (Direct Access)`);
});
