import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const image = readFileSync(new URL('./entry.png', import.meta.url));
console.log(JSON.stringify({ bytes: image.length, sha256: createHash('sha256').update(image).digest('hex') }));
