# Image Integration Guide - Mutiny Labs Website

## Quick Start: How to Add Your Images

Once you've created your images, follow this guide to integrate them into the website.

---

## Step 1: Prepare Your Images

### Create a folder structure:
```
mutiny website/
├── images/
│   ├── hero/
│   │   └── hero-ecosystem.webp
│   ├── services/
│   │   ├── digital-strategy.webp
│   │   ├── experience-design.webp
│   │   ├── development.webp
│   │   ├── growth-scale.webp
│   │   ├── transformation.webp
│   │   └── innovation-lab.webp
│   ├── about/
│   │   ├── gino-profile.jpg
│   │   ├── team-avatar.png
│   │   ├── values-innovation.svg
│   │   ├── values-partnership.svg
│   │   ├── values-expertise.svg
│   │   ├── values-growth.svg
│   │   ├── values-data-driven.svg
│   │   ├── values-human-centered.svg
│   │   └── story-journey.webp
│   ├── work/
│   │   ├── case-mozilla.webp
│   │   ├── case-hotel-indigo.webp
│   │   ├── case-banking.webp
│   │   ├── case-ecommerce.webp
│   │   ├── case-youth.webp
│   │   ├── client-microsoft.svg
│   │   ├── client-mozilla.svg
│   │   ├── client-toyota.svg
│   │   ├── client-intercontinental.svg
│   │   ├── client-honda.svg
│   │   ├── client-bacardi.svg
│   │   ├── client-oriental-bank.svg
│   │   └── client-tourism.svg
│   └── misc/
│       ├── favicon.ico
│       └── logo-mark.svg
```

---

## Step 2: Update Homepage (mutiny-labs-website.html)

### Hero Section Image
Find this section around line 750 and replace the emoji placeholder:

**BEFORE:**
```html
<div class="hero-card">
    <h3>Growing Together</h3>
    <!-- ... content ... -->
</div>
```

**AFTER:**
```html
<div class="hero-card">
    <h3>Growing Together</h3>
    <!-- Add image above if desired -->
    <picture>
        <source srcset="images/hero/hero-ecosystem.webp" type="image/webp">
        <img src="images/hero/hero-ecosystem-fallback.jpg" alt="Digital ecosystem illustration" style="max-width: 100%; border-radius: 20px; margin-bottom: 30px;">
    </picture>
    <!-- ... existing content ... -->
</div>
```

---

## Step 3: Update Services Page (services.html)

### Service Visual Replacements
Find the `.service-visual` divs (around lines 351, 356, etc.) and replace emoji:

**BEFORE:**
```html
<div class="service-visual">🎯</div>
```

**AFTER:**
```html
<div class="service-visual">
    <picture>
        <source srcset="images/services/digital-strategy.webp" type="image/webp">
        <img src="images/services/digital-strategy.png" alt="Digital Strategy Service" style="max-width: 100%; height: auto;">
    </picture>
</div>
```

### Repeat for all 6 services:
1. Digital Strategy (line 351)
2. Experience Design (line 356)
3. Development (line 395)
4. Growth & Scale (line 400)
5. Transformation (line 439)
6. Innovation Lab (line 444)

---

## Step 4: Update About Page (about.html)

### Values Icons
Find `.value-icon` divs (around line 479+) and replace emoji:

**BEFORE:**
```html
<div class="value-icon">🚀</div>
```

**AFTER:**
```html
<div class="value-icon">
    <picture>
        <source srcset="images/about/values-innovation.svg" type="image/svg+xml">
        <img src="images/about/values-innovation.png" alt="Innovation icon" style="max-width: 100%; height: auto;">
    </picture>
</div>
```

### Leadership Avatars
Find `.leader-avatar` divs (around line 518+):

**BEFORE:**
```html
<div class="leader-avatar">👨‍💼</div>
```

**AFTER:**
```html
<div class="leader-avatar" style="background: url('images/about/gino-profile.jpg') center/cover !important;">
    <!-- Image background replaces emoji -->
</div>
```

**OR** for background image, update CSS:
```css
.leader-avatar {
    background: linear-gradient(135deg, #C856D7 0%, #B845C6 100%), url('images/about/gino-profile.jpg') center/cover;
    background-size: cover;
}
```

### Second card (Team Avatar):
```html
<div class="leader-avatar" style="background: url('images/about/team-avatar.png') center/cover !important;">
    <!-- Image background -->
</div>
```

---

## Step 5: Update Work Page (work.html)

### Case Study Visuals
Find `.case-visual` divs (around lines 426, 433, 494, 501, 562) and replace emoji:

**BEFORE:**
```html
<div class="case-visual">🦊</div>
```

**AFTER:**
```html
<div class="case-visual">
    <picture>
        <source srcset="images/work/case-mozilla.webp" type="image/webp">
        <img src="images/work/case-mozilla.png" alt="Mozilla Firefox case study" style="max-width: 100%; height: auto; border-radius: 20px;">
    </picture>
</div>
```

### Client Logos
Find `.client-logo` divs (around lines 574-602) and replace emoji:

**BEFORE:**
```html
<div class="client-logo">🔵</div>
```

**AFTER:**
```html
<div class="client-logo">
    <picture>
        <source srcset="images/work/client-microsoft.svg" type="image/svg+xml">
        <img src="images/work/client-microsoft.png" alt="Microsoft logo" style="max-width: 80%; height: auto; filter: opacity(0.7);">
    </picture>
</div>
```

---

## Step 6: Add CSS for Image Styling

Add this to your stylesheet (optional, for better control):

```css
/* Image Optimization */
img {
    max-width: 100%;
    height: auto;
    display: block;
}

picture {
    display: block;
    width: 100%;
}

/* Service/Case Study Images */
.service-visual img,
.case-visual img {
    border-radius: 20px;
    object-fit: cover;
}

/* Client Logos */
.client-logo img {
    opacity: 0.7;
    transition: opacity 0.3s;
}

.client-logo:hover img {
    opacity: 1;
}

/* Leadership Avatars */
.leader-avatar {
    background-size: cover;
    background-position: center;
}
```

---

## Step 7: File Naming Reference

Use these exact file names for easy implementation:

### Hero Images
- `images/hero/hero-ecosystem.webp`

### Service Images
- `images/services/digital-strategy.webp`
- `images/services/experience-design.webp`
- `images/services/development.webp`
- `images/services/growth-scale.webp`
- `images/services/transformation.webp`
- `images/services/innovation-lab.webp`

### About Page
- `images/about/gino-profile.jpg`
- `images/about/team-avatar.png`
- `images/about/values-innovation.svg`
- `images/about/values-partnership.svg`
- `images/about/values-expertise.svg`
- `images/about/values-growth.svg`
- `images/about/values-data-driven.svg`
- `images/about/values-human-centered.svg`
- `images/about/story-journey.webp`

### Work Page Case Studies
- `images/work/case-mozilla.webp`
- `images/work/case-hotel-indigo.webp`
- `images/work/case-banking.webp`
- `images/work/case-ecommerce.webp`
- `images/work/case-youth.webp`

### Client Logos
- `images/work/client-microsoft.svg`
- `images/work/client-mozilla.svg`
- `images/work/client-toyota.svg`
- `images/work/client-intercontinental.svg`
- `images/work/client-honda.svg`
- `images/work/client-bacardi.svg`
- `images/work/client-oriental-bank.svg`
- `images/work/client-tourism.svg`

---

## Step 8: Optimization Checklist

Before deploying, ensure:

- [ ] All images are WebP or optimized formats
- [ ] File sizes are under specified limits
- [ ] Images are responsive (multiple sizes if needed)
- [ ] Alt text is descriptive
- [ ] Images are in correct folders
- [ ] File paths match exactly in HTML
- [ ] Fallback JPG/PNG provided for WebP
- [ ] Test on mobile, tablet, and desktop
- [ ] Check Google PageSpeed Insights
- [ ] Verify images display correctly

---

## Quick Copy-Paste Templates

### Hero Section
```html
<picture>
    <source srcset="images/hero/hero-ecosystem.webp" type="image/webp">
    <img src="images/hero/hero-ecosystem.jpg" alt="Digital ecosystem transformation illustration" style="max-width: 100%; height: auto; border-radius: 20px;">
</picture>
```

### Service Cards
```html
<div class="service-visual">
    <picture>
        <source srcset="images/services/SERVICE_NAME.webp" type="image/webp">
        <img src="images/services/SERVICE_NAME.png" alt="SERVICE_NAME illustration" style="max-width: 100%; height: auto;">
    </picture>
</div>
```

### Case Studies
```html
<div class="case-visual">
    <picture>
        <source srcset="images/work/case-PROJECTNAME.webp" type="image/webp">
        <img src="images/work/case-PROJECTNAME.png" alt="PROJECTNAME case study" style="max-width: 100%; height: auto; border-radius: 20px;">
    </picture>
</div>
```

### Client Logos
```html
<div class="client-logo">
    <picture>
        <source srcset="images/work/client-CLIENTNAME.svg" type="image/svg+xml">
        <img src="images/work/client-CLIENTNAME.png" alt="CLIENT NAME logo" style="max-width: 80%; height: auto;">
    </picture>
</div>
```

---

## Troubleshooting

**Images not showing:**
- Verify file paths are correct
- Check file names match exactly (case-sensitive)
- Ensure `images/` folder is in same directory as HTML files
- Check browser console for 404 errors

**Images too large:**
- Use TinyPNG or Squoosh to compress
- Convert JPG to WebP format
- Reduce dimensions if oversized
- Use image optimization tools

**Images look blurry:**
- Ensure DPI is 72 (web standard)
- Use double-size images for high-DPI displays
- Try increasing sharpness in editor before export

**Client logos need adjusting:**
- Use `filter: opacity(0.7)` in CSS
- Adjust with `mix-blend-mode: multiply` or `screen`
- Create versions with transparent backgrounds

---

## Deployment

Once images are integrated:

1. Test locally in browser
2. Test responsive design (mobile/tablet)
3. Run through Google PageSpeed Insights
4. Run `./deploy.sh YOUR_PROJECT_ID` to deploy to Google Cloud Run
5. Verify images appear correctly on live site

---

## Image Optimization Tools

- **TinyPNG/TinyJPG**: https://tinypng.com/ (free compression)
- **Squoosh**: https://squoosh.app/ (Google's image optimizer)
- **ImageMagick**: Command line batch processing
- **Cloudinary**: Cloud-based image management
- **Sharp**: Node.js image processing library

---

## Support

For questions about image integration:
- Review IMAGE_SPECIFICATIONS.md for detailed specs
- Check file paths and naming conventions
- Test in multiple browsers
- Use browser DevTools to debug

Happy image integration!
