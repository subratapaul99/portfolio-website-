Subrata Paul — Portfolio Website

Personal portfolio of Subrata Paul, B.Tech Computer Science student (RVS College of Engineering & Technology, Jamshedpur) and aspiring data analyst / AI-ML engineer. It presents my internships, projects, skills, certifications and achievements in a single responsive page.

Highlights
Experience timeline: IBM SkillsBuild (AI), Microsoft (AI Azure), InternPe (Python), plus upcoming Oasis Infobyte (Data Analytics) and CodeAlpha (Cloud Computing) internships.
Projects: E-Commerce Sales Analysis with AI Prediction, Trading Journal (MERN), Business Sales Prediction, Todo (Django), Ria Designs and this portfolio.
Credentials & achievements: internship certificates, IBM AI Fundamentals badge, NISM / SEBI test, IoT workshop, Google Student Ambassador Music Night, and painting certificates. Each opens in a full-size lightbox.
Polished UI: dark mode, scroll progress bar, mobile menu, typing animation, scroll-reveal effects, photo gallery slider, back-to-top button.
Accessibility & performance: keyboard-friendly controls, skip link, reduced-motion support, lazy-loaded images, no build step.
Tech stack

HTML, CSS and vanilla JavaScript in a single index.html. Fonts come from Google Fonts (Syne, Plus Jakarta Sans). EmailJS is optional for the contact form.

Project structure
portfolio-website-/
├── index.html        # the entire site (HTML, CSS, JS)
├── resume.pdf        # linked from the "Resume" button
├── image1–6.jpeg     # gallery photos
├── certs/            # certificate images shown in Achievements
├── offers/           # internship offer letters (image + PDF)
├── server.py         # optional Flask backend from an earlier version (not used by the live site)
└── requirements.txt  # Python dependencies for server.py
Run locally

No installation is needed. Open index.html in a browser, or serve the folder:

bash
python -m http.server 8000
# then visit http://localhost:8000
Deploy on GitHub Pages
Push the repository to GitHub.
Go to Settings → Pages.
Under Build and deployment, choose Deploy from a branch, select main and / (root), then save.
The site will be available at https://<username>.github.io/portfolio-website-/ after a minute or two.
Customising
Gallery photos: edit the galleryData array near the bottom of index.html (file name and caption for each image).
Certificates: add an image to certs/, then add a card with the ach(...) pattern used in the Achievements section.
Contact form: until EmailJS is configured, the form opens the visitor's email app. To send directly from the page, create an account at emailjs.com and replace YOUR_SERVICE_ID, YOUR_TEMPLATE_ID and YOUR_PUBLIC_KEY in index.html.
Colours: change the CSS variables in :root (light) and body.dark (dark) at the top of the stylesheet.
Contact
Email: paulsubrata309@gmail.com
GitHub: @subratapaul99
Location: Jamshedpur, Jharkhand, India

© 2026 Subrata Paul. The code is free to learn from; please don't copy the personal content, photos or certificates.
