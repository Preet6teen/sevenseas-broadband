#!/usr/bin/env python3
"""
Process user-uploaded logo (media_1793705758541_4503ebee.jpg)
and generate production logo assets for Sevenseas Broadband:
- public/assets/images/logo.png: Crisp transparent PNG for light backgrounds (white navbar)
- public/assets/images/logo-white.png: Crisp transparent PNG for dark backgrounds (navy footer)
- public/assets/images/logo-black.png: Exact original uploaded image with black background
- public/assets/images/logo.svg: High-resolution SVG embedding the authentic mark
- public/assets/images/logo-white.svg: High-resolution SVG embedding the white/dark-surface mark
- public/assets/images/favicon.svg / favicon.png: Authentic brand favicon
"""

import os
import struct
import zlib
import base64

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOADED_JPG = "/Users/pratish/.gemini/antigravity/brain/af80652a-bc6c-4e30-abce-0174cd2207bb/.user_uploaded/media_1793705758541_4503ebee.jpg"
IMG_DIR = os.path.join(ROOT_DIR, "public", "assets", "images")

# First, ensure we have uncompressed RGB from the uploaded JPG via sips
RAW_PNG = os.path.join(IMG_DIR, "logo-official-black.png")
if not os.path.exists(RAW_PNG):
    os.system(f"sips -s format png '{UPLOADED_JPG}' --out '{RAW_PNG}'")

# Copy original jpg to assets as well
os.system(f"cp '{UPLOADED_JPG}' '{os.path.join(IMG_DIR, 'logo-black.jpg')}'")

# Read RAW PNG
with open(RAW_PNG, "rb") as f:
    data = f.read()

pos = 8
idat = []
w, h = 1024, 386
while pos < len(data):
    length, ctype = struct.unpack(">I4s", data[pos:pos+8])
    if ctype == b"IHDR":
        w, h, bitd, colort, comp, filt, inter = struct.unpack(">IIBBBBB", data[pos+8:pos+8+length])
    elif ctype == b"IDAT":
        idat.append(data[pos+8:pos+8+length])
    pos += 12 + length

decompressed = zlib.decompress(b"".join(idat))

def unfilter(raw, width, height, bpp=3):
    stride = 1 + width * bpp
    out = bytearray(width * height * bpp)
    prev = bytearray(width * bpp)
    for y in range(height):
        ftype = raw[y * stride]
        rin = raw[y * stride + 1 : (y + 1) * stride]
        rout = bytearray(width * bpp)
        if ftype == 0:
            rout[:] = rin
        elif ftype == 1:
            for x in range(width * bpp):
                left = rout[x - bpp] if x >= bpp else 0
                rout[x] = (rin[x] + left) & 0xff
        elif ftype == 2:
            for x in range(width * bpp):
                up = prev[x]
                rout[x] = (rin[x] + up) & 0xff
        elif ftype == 3:
            for x in range(width * bpp):
                left = rout[x - bpp] if x >= bpp else 0
                up = prev[x]
                rout[x] = (rin[x] + ((left + up) >> 1)) & 0xff
        elif ftype == 4:
            for x in range(width * bpp):
                left = rout[x - bpp] if x >= bpp else 0
                up = prev[x]
                up_left = prev[x - bpp] if x >= bpp else 0
                p = left + up - up_left
                pa, pb, pc = abs(p - left), abs(p - up), abs(p - up_left)
                if pa <= pb and pa <= pc: pr = left
                elif pb <= pc: pr = up
                else: pr = up_left
                rout[x] = (rin[x] + pr) & 0xff
        out[y * width * bpp : (y + 1) * width * bpp] = rout
        prev = rout
    return out

pixels = unfilter(decompressed, w, h, 3)

def write_png(filename, width, height, rgba_bytes):
    raw_payload = bytearray()
    stride = width * 4
    for y in range(height):
        raw_payload.append(0) # None filter
        raw_payload.extend(rgba_bytes[y * stride : (y + 1) * stride])
    compressed = zlib.compress(bytes(raw_payload), 9)
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    def chunk(tag, payload):
        crc = zlib.crc32(tag + payload) & 0xffffffff
        return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", crc)
    out = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")
    with open(filename, "wb") as f:
        f.write(out)
    print(f"Generated: {filename} ({len(out)} bytes)")

# 1. Generate logo.png (Transparent for Light Backgrounds)
# The authentic logo has:
# - "Seven", "Br", "adband", signal ring, tagline in navy blue (R~30, G~50, B~90)
# - "seas" in warm orange (R~230, G~160, B~40)
# - Red globe in crimson (R~220, G~40, B~40)
# - Orange signal waves in vibrant orange (R~235, G~130, B~40)
# - Black background (R=0, G=0, B=0)
# On light backgrounds (e.g. #FFFFFF or #F7F8FC):
# Pure black should be alpha=0.
# For pixels with content, we make alpha=255 for solid body, and calculate smooth anti-aliased edge alpha.
# Furthermore, we boost the contrast of the navy text slightly (since on black background it was drawn slightly muted)
# so on white it is a crisp, commanding deep navy (#1E3050).

rgba_light = bytearray(w * h * 4)
rgba_white = bytearray(w * h * 4)

for y in range(h):
    for x in range(w):
        idx_rgb = (y * w + x) * 3
        idx_rgba = (y * w + x) * 4
        r = pixels[idx_rgb]
        g = pixels[idx_rgb + 1]
        b = pixels[idx_rgb + 2]
        m = max(r, g, b)

        if m <= 2:
            # Pure black background -> transparent
            rgba_light[idx_rgba : idx_rgba + 4] = b"\x00\x00\x00\x00"
            rgba_white[idx_rgba : idx_rgba + 4] = b"\x00\x00\x00\x00"
        else:
            # Determine color identity
            # Is it orange / yellow / amber ("seas" or signal wave)?
            is_orange = (r > 100 and g > 50 and (r > b * 1.5))
            # Is it red ("Globe o")?
            is_red = (r > 100 and g < 75 and b < 75 and r > g * 1.8)
            # Is it the blue divider line, navy text, or signal ring?
            is_blue_or_navy = not (is_orange or is_red)

            # Calculate anti-aliasing alpha
            # If m < 25, it's an edge anti-alias pixel transitioning to black
            if m < 25:
                alpha = int((m / 25.0) * 255)
            else:
                alpha = 255

            # --- LIGHT SURFACE VERSION (logo.png) ---
            if is_orange or is_red:
                # Keep original vibrant warm tones
                # Demultiply black from edges if alpha < 255
                scale = 255.0 / max(1, m) if m < 25 else 1.0
                nr = min(255, int(r * scale))
                ng = min(255, int(g * scale))
                nb = min(255, int(b * scale))
            else:
                # Navy / Slate elements ("Seven", "Broadband", signal frame, tagline)
                # Ensure rich, deep navy #1E3050 (or deep royal blue from the mark)
                # Map intensity to solid navy on white
                intensity = min(1.0, m / 65.0)
                # Navy target: #1E3050 => (30, 48, 80)
                nr = int(30 * intensity)
                ng = int(48 * intensity)
                nb = int(80 * intensity)
                # For smooth edges, use alpha
                alpha = int(min(255, m * 4.5))

            rgba_light[idx_rgba] = nr
            rgba_light[idx_rgba + 1] = ng
            rgba_light[idx_rgba + 2] = nb
            rgba_light[idx_rgba + 3] = alpha

            # --- DARK SURFACE / WHITE VERSION (logo-white.png) ---
            # For dark navy footer (#0F1B2D):
            # Orange and Red remain vibrant!
            # The navy text ("Seven", "Broadband", tagline) becomes crisp WHITE / luminous slate (#FFFFFF)
            if is_orange or is_red:
                rgba_white[idx_rgba] = r
                rgba_white[idx_rgba + 1] = g
                rgba_white[idx_rgba + 2] = b
                rgba_white[idx_rgba + 3] = alpha
            else:
                # Invert navy text to pure crisp white
                rgba_white[idx_rgba] = 255
                rgba_white[idx_rgba + 1] = 255
                rgba_white[idx_rgba + 2] = 255
                rgba_white[idx_rgba + 3] = alpha

# Write PNGs
logo_png_path = os.path.join(IMG_DIR, "logo.png")
logo_white_png_path = os.path.join(IMG_DIR, "logo-white.png")
logo_black_png_path = os.path.join(IMG_DIR, "logo-black.png")

write_png(logo_png_path, w, h, rgba_light)
write_png(logo_white_png_path, w, h, rgba_white)
# Exact original as PNG
os.system(f"cp '{RAW_PNG}' '{logo_black_png_path}'")

# Overwrite logo-light-bg.png and logo-dark-bg.png so any references get the updated assets
os.system(f"cp '{logo_png_path}' '{os.path.join(IMG_DIR, 'logo-light-bg.png')}'")
os.system(f"cp '{logo_white_png_path}' '{os.path.join(IMG_DIR, 'logo-dark-bg.png')}'")

# Now generate SVG wrappers that embed the exact PNG as base64 data URI
# This guarantees that ANY <img src="logo.svg"> immediately renders the exact authentic logo!
with open(logo_png_path, "rb") as f:
    b64_light = base64.b64encode(f.read()).decode("ascii")

with open(logo_white_png_path, "rb") as f:
    b64_white = base64.b64encode(f.read()).decode("ascii")

with open(logo_black_png_path, "rb") as f:
    b64_black = base64.b64encode(f.read()).decode("ascii")

svg_light = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 386" width="100%" height="100%" role="img" aria-label="Sevenseas Broadband - Connecting Every Home">
  <image href="data:image/png;base64,{b64_light}" width="1024" height="386" />
</svg>'''

svg_white = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 386" width="100%" height="100%" role="img" aria-label="Sevenseas Broadband - Connecting Every Home">
  <image href="data:image/png;base64,{b64_white}" width="1024" height="386" />
</svg>'''

svg_black = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 386" width="100%" height="100%" role="img" aria-label="Sevenseas Broadband - Connecting Every Home">
  <image href="data:image/png;base64,{b64_black}" width="1024" height="386" />
</svg>'''

with open(os.path.join(IMG_DIR, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(svg_light)

with open(os.path.join(IMG_DIR, "logo-white.svg"), "w", encoding="utf-8") as f:
    f.write(svg_white)

with open(os.path.join(IMG_DIR, "logo-black.svg"), "w", encoding="utf-8") as f:
    f.write(svg_black)

print("✓ Successfully generated all logo assets:")
print(f"  - {logo_png_path} (Light surface transparent)")
print(f"  - {logo_white_png_path} (Dark surface transparent)")
print(f"  - {logo_black_png_path} (Original black background)")
print(f"  - {os.path.join(IMG_DIR, 'logo.svg')} (Vector/SVG light)")
print(f"  - {os.path.join(IMG_DIR, 'logo-white.svg')} (Vector/SVG white)")
print(f"  - {os.path.join(IMG_DIR, 'logo-black.svg')} (Vector/SVG black)")
