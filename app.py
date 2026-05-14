from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Sohan H G | Software Developer</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:       #060810;
      --surface:  #0d1020;
      --card:     #111525;
      --border:   #1e2540;
      --accent:   #00e5ff;
      --accent2:  #7c3aed;
      --text:     #e8eaf6;
      --muted:    #6b7498;
      --mono:     'Space Mono', monospace;
      --sans:     'Syne', sans-serif;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--sans);
      overflow-x: hidden;
    }

    /* ── SCROLLBAR ── */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 2px; }

    /* ── GRID BACKGROUND ── */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(0,229,255,.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,229,255,.03) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    /* ── NAV ── */
    nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.2rem 4rem;
      background: rgba(6,8,16,.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }

    .nav-logo {
      font-family: var(--mono);
      font-size: .85rem;
      color: var(--accent);
      letter-spacing: .1em;
    }
    .nav-logo span { color: var(--muted); }

    .nav-links { display: flex; gap: 2rem; }
    .nav-links a {
      font-family: var(--mono);
      font-size: .78rem;
      color: var(--muted);
      text-decoration: none;
      letter-spacing: .08em;
      transition: color .2s;
    }
    .nav-links a:hover { color: var(--accent); }

    /* ── HERO ── */
    #hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 0 4rem;
      position: relative;
      z-index: 1;
    }

    .hero-tag {
      font-family: var(--mono);
      font-size: .78rem;
      color: var(--accent);
      letter-spacing: .2em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
      opacity: 0;
      animation: fadeUp .6s .2s forwards;
    }

    .hero-name {
      font-size: clamp(3.5rem, 9vw, 8rem);
      font-weight: 800;
      line-height: .95;
      letter-spacing: -.02em;
      opacity: 0;
      animation: fadeUp .6s .4s forwards;
      margin: 0 0 2rem 0;
    }

    .hero-name-accent {
      -webkit-text-stroke: 1px var(--accent);
      color: transparent;
      display: block;
    }

    .hero-sub {
      margin: 0 0 2.5rem 0;
      font-family: var(--mono);
      font-size: .95rem;
      color: var(--muted);
      max-width: 520px;
      line-height: 1.8;
      opacity: 0;
      animation: fadeUp .6s .6s forwards;
    }

    .hero-cta {
      display: flex;
      gap: 1rem;
      margin-top: 0;
      opacity: 0;
      animation: fadeUp .6s .7s forwards;
    }

    .btn {
      display: inline-block;
      padding: .75rem 2rem;
      border-radius: 2px;
      font-family: var(--mono);
      font-size: .8rem;
      letter-spacing: .08em;
      cursor: pointer;
      text-decoration: none;
      transition: all .25s;
    }
    .btn-primary {
      background: var(--accent);
      color: var(--bg);
      font-weight: 700;
    }
    .btn-primary:hover { background: #00b8cc; transform: translateY(-2px); }

    .btn-ghost {
      border: 1px solid var(--border);
      color: var(--muted);
    }
    .btn-ghost:hover { border-color: var(--accent); color: var(--accent); }

    .hero-orb {
      position: absolute;
      right: -10%;
      top: 50%;
      transform: translateY(-50%);
      width: 600px;
      height: 600px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0,229,255,.08) 0%, transparent 70%);
      pointer-events: none;
    }

    .hero-profile {
      display: flex;
      gap: 3rem;
      align-items: center;
      margin-top: 1rem;
      justify-content: space-between;
    }

    .hero-content {
      display: flex;
      flex-direction: column;
      opacity: 0;
      animation: fadeUp .6s .5s forwards;
    }

    .hero-profile-img {
      width: 420px;
      height: 420px;
      border-radius: 12px;
      object-fit: cover;
      border: 3px solid var(--accent);
      box-shadow: 0 0 50px rgba(0,229,255,.3);
      opacity: 0;
      animation: fadeUp .6s .6s forwards;
      flex-shrink: 0;
    }

    .hero-right {
      display: none;
    }

    .hero-name-lower {
      display: none;
    }

    /* ── SECTIONS ── */
    section {
      position: relative;
      z-index: 1;
      padding: 6rem 4rem;
    }

    .section-label {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 3rem;
    }
    .section-label::before {
      content: '';
      width: 2rem;
      height: 1px;
      background: var(--accent);
    }
    .section-label span {
      font-family: var(--mono);
      font-size: .75rem;
      letter-spacing: .2em;
      color: var(--accent);
      text-transform: uppercase;
    }

    h2 {
      font-size: clamp(2rem, 4vw, 3.5rem);
      font-weight: 800;
      letter-spacing: -.02em;
      margin-bottom: 1rem;
    }

    /* ── ABOUT ── */
    #about .about-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4rem;
      align-items: center;
    }

    .about-text {
      font-size: 1.05rem;
      color: var(--muted);
      line-height: 1.9;
    }

    .about-text strong { color: var(--text); }

    .skills-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: .75rem;
    }

    .skill-chip {
      background: var(--card);
      border: 1px solid var(--border);
      padding: .6rem 1rem;
      border-radius: 2px;
      font-family: var(--mono);
      font-size: .78rem;
      color: var(--muted);
      display: flex;
      align-items: center;
      gap: .5rem;
      transition: all .2s;
    }
    .skill-chip::before {
      content: '▸';
      color: var(--accent);
      font-size: .7rem;
    }
    .skill-chip:hover {
      border-color: var(--accent);
      color: var(--text);
      transform: translateX(4px);
    }

    /* ── PROJECTS ── */
    #projects .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.5rem;
    }

    .project-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2rem;
      position: relative;
      overflow: hidden;
      transition: border-color .3s, transform .3s;
    }

    .project-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      transform: scaleX(0);
      transform-origin: left;
      transition: transform .3s;
    }

    .project-card:hover { border-color: var(--accent); transform: translateY(-4px); }
    .project-card:hover::before { transform: scaleX(1); }

    .project-date {
      font-family: var(--mono);
      font-size: .72rem;
      color: var(--muted);
      letter-spacing: .08em;
      margin-bottom: .75rem;
    }

    .project-title {
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: .75rem;
    }

    .project-stack {
      display: flex;
      flex-wrap: wrap;
      gap: .4rem;
      margin-bottom: 1.25rem;
    }

    .tag {
      background: rgba(0,229,255,.08);
      border: 1px solid rgba(0,229,255,.2);
      color: var(--accent);
      font-family: var(--mono);
      font-size: .68rem;
      padding: .25rem .6rem;
      border-radius: 2px;
      letter-spacing: .06em;
    }

    .project-bullets {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: .5rem;
    }

    .project-bullets li {
      font-size: .88rem;
      color: var(--muted);
      line-height: 1.6;
      padding-left: 1rem;
      position: relative;
    }
    .project-bullets li::before {
      content: '—';
      position: absolute;
      left: 0;
      color: var(--accent);
      font-size: .7rem;
    }

    /* ── EXPERIENCE ── */
    #experience .exp-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2.5rem;
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 0 2rem;
      position: relative;
    }

    .exp-marker {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0;
    }

    .exp-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 12px var(--accent);
      flex-shrink: 0;
      margin-top: 5px;
    }

    .exp-line {
      width: 1px;
      flex: 1;
      background: var(--border);
      margin-top: 4px;
    }

    .exp-role {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: .25rem;
    }

    .exp-company {
      font-family: var(--mono);
      font-size: .8rem;
      color: var(--accent);
      letter-spacing: .06em;
      margin-bottom: .25rem;
    }

    .exp-period {
      font-family: var(--mono);
      font-size: .75rem;
      color: var(--muted);
      margin-bottom: 1.25rem;
    }

    .exp-bullets {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: .5rem;
    }

    .exp-bullets li {
      font-size: .9rem;
      color: var(--muted);
      line-height: 1.7;
      padding-left: 1rem;
      position: relative;
    }
    .exp-bullets li::before {
      content: '▸';
      position: absolute;
      left: 0;
      color: var(--accent);
      font-size: .75rem;
    }

    /* ── EDUCATION ── */
    #education .edu-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }

    .edu-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2rem;
      transition: border-color .3s;
    }
    .edu-card:hover { border-color: var(--accent2); }

    .edu-degree {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: .5rem;
    }

    .edu-school {
      font-family: var(--mono);
      font-size: .8rem;
      color: var(--accent);
      letter-spacing: .05em;
      margin-bottom: .4rem;
    }

    .edu-meta {
      display: flex;
      justify-content: space-between;
      font-family: var(--mono);
      font-size: .75rem;
      color: var(--muted);
      margin-top: .75rem;
    }

    .cgpa {
      color: var(--accent);
      font-weight: 700;
    }

    /* ── CONTACT ── */
    #contact {
      text-align: center;
    }

    #contact h2 { margin-bottom: 1rem; }
    #contact p {
      color: var(--muted);
      font-family: var(--mono);
      font-size: .85rem;
      margin-bottom: 2.5rem;
      line-height: 1.8;
    }

    .contact-links {
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .contact-link {
      display: flex;
      align-items: center;
      gap: .5rem;
      background: var(--card);
      border: 1px solid var(--border);
      padding: .75rem 1.5rem;
      border-radius: 2px;
      color: var(--muted);
      text-decoration: none;
      font-family: var(--mono);
      font-size: .8rem;
      letter-spacing: .06em;
      transition: all .25s;
    }
    .contact-link:hover {
      border-color: var(--accent);
      color: var(--accent);
      transform: translateY(-2px);
    }

    /* ── FOOTER ── */
    footer {
      border-top: 1px solid var(--border);
      padding: 2rem 4rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--mono);
      font-size: .72rem;
      color: var(--muted);
      position: relative;
      z-index: 1;
    }

    /* ── DIVIDER ── */
    .section-divider {
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--border), transparent);
      margin: 0 4rem;
    }

    /* ── ANIMATIONS ── */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(24px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    .reveal {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity .6s ease, transform .6s ease;
    }
    .reveal.visible {
      opacity: 1;
      transform: translateY(0);
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 768px) {
      nav { padding: 1rem 1.5rem; }
      .nav-links { display: none; }
      #hero, section { padding: 5rem 1.5rem; }
      #about .about-grid { grid-template-columns: 1fr; }
      #education .edu-grid { grid-template-columns: 1fr; }
      footer { flex-direction: column; gap: .75rem; text-align: center; }
      .section-divider { margin: 0 1.5rem; }
    }
  </style>
</head>
<body>

  <!-- NAV -->
  <nav>
    <div class="nav-logo"><span>~/</span>sohan-hg</div>
    <div class="nav-links">
      <a href="#about">About</a>
      <a href="#projects">Projects</a>
      <a href="#experience">Experience</a>
      <a href="#education">Education</a>
      <a href="#contact">Contact</a>
    </div>
  </nav>

  <!-- HERO -->
  <section id="hero">
    <div class="hero-tag">Software Developer </div>
    <div class="hero-profile">
      <div class="hero-content">
        <h1 class="hero-name">
          Sohan<br>
          <span class="hero-name-accent">H G</span>
        </h1>
        <p class="hero-sub">
          Computer Science undergraduate — building full-stack &amp;<br>
          data-driven applications with Java, Python &amp; modern web tech.
        </p>
        <div class="hero-cta">
          <a href="#projects" class="btn btn-primary">View Projects</a>
          <a href="#contact" class="btn btn-ghost">Get in Touch</a>
        </div>
      </div>
      <img src="/static/profile.jpeg" alt="Sohan Profile" class="hero-profile-img">
    </div>
    <div class="hero-orb"></div>
  </section>

  <div class="section-divider"></div>

  <!-- ABOUT -->
  <section id="about">
    <div class="section-label"><span>01 / About</span></div>
    <div class="about-grid">
      <div>
        <h2>Building things that matter.</h2>
        <p class="about-text" style="margin-top:1.5rem">
          Detail-oriented Computer Science undergraduate with a strong foundation
          in <strong>software development</strong>, <strong>data structures</strong>, and
          <strong>web technologies</strong>. Hands-on experience building full-stack and
          data-driven applications through academic and real-world projects.
          <br><br>
          Demonstrates strong analytical thinking, problem-solving ability,
          and effective written and verbal communication skills.
        </p>
      </div>
      <div>
        <p style="font-family:var(--mono);font-size:.75rem;color:var(--accent);letter-spacing:.1em;margin-bottom:1rem">// TECH STACK</p>
        <div class="skills-grid">
          <div class="skill-chip">Java</div>
          <div class="skill-chip">Python</div>
          <div class="skill-chip">HTML5 &amp; CSS3</div>
          <div class="skill-chip">React.js</div>
          <div class="skill-chip">Flask</div>
          <div class="skill-chip">MySQL</div>
          <div class="skill-chip">MongoDB</div>
          <div class="skill-chip">PHP</div>
          <div class="skill-chip">OOPS</div>
          <div class="skill-chip">DBMS</div>
          <div class="skill-chip">Servlets / JSP</div>
          <div class="skill-chip">Operating Systems</div>
        </div>
      </div>
    </div>
  </section>

  <div class="section-divider"></div>

  <!-- PROJECTS -->
  <section id="projects">
    <div class="section-label"><span>02 / Projects</span></div>
    <h2>Things I've Built</h2>
    <br>
    <div class="projects-grid reveal">

      <div class="project-card">
        <div class="project-date">Apr 2026</div>
        <div class="project-title">Food Delivery Web Application</div>
        <div class="project-stack">
          <span class="tag">Java</span>
          <span class="tag">Servlets</span>
          <span class="tag">JSP</span>
          <span class="tag">MySQL</span>
          <span class="tag">HTML/CSS</span>
        </div>
        <ul class="project-bullets">
          <li>Full-stack food delivery platform with user auth, restaurant browsing, menu filtering, and session-based cart with real-time quantity updates.</li>
          <li>End-to-end order placement with coupon discounts, multiple payment options, order history, and live order tracking with auto-refresh.</li>
          <li>Additional features: wishlist management, review submission, and responsive UI with dark mode support across all pages.</li>
        </ul>
      </div>

      <div class="project-card">
        <div class="project-date">Nov 2025</div>
        <div class="project-title">Hybrid Malware Detection System</div>
        <div class="project-stack">
          <span class="tag">React.js</span>
          <span class="tag">Python</span>
          <span class="tag">Flask</span>
          <span class="tag">Machine Learning</span>
        </div>
        <ul class="project-bullets">
          <li>Web-based Android malware detection system using hybrid static and dynamic feature analysis.</li>
          <li>Random Forest ML model to classify benign and malicious APK files with high accuracy.</li>
          <li>Evaluated and improved model performance metrics for more reliable detection outcomes.</li>
        </ul>
      </div>

      <div class="project-card">
        <div class="project-date">Jun 2025</div>
        <div class="project-title">KED Online Portal</div>
        <div class="project-stack">
          <span class="tag">PHP</span>
          <span class="tag">MySQL</span>
          <span class="tag">HTML/CSS</span>
          <span class="tag">XAMPP</span>
        </div>
        <ul class="project-bullets">
          <li>Web portal for managing departmental documents and notices.</li>
          <li>Admin and Employee modules with authentication and full CRUD operations.</li>
          <li>Designed database schema and conducted module testing for system reliability.</li>
        </ul>
      </div>

    </div>
  </section>

  <div class="section-divider"></div>

  <!-- EXPERIENCE -->
  <section id="experience">
    <div class="section-label"><span>03 / Experience</span></div>
    <h2>Where I've Worked</h2>
    <br>
    <div class="exp-card reveal">
      <div class="exp-marker">
        <div class="exp-dot"></div>
        <div class="exp-line"></div>
      </div>
      <div>
        <div class="exp-role">Software Development Intern</div>
        <div class="exp-company">Tap Academy — Bengaluru</div>
        <div class="exp-period">Feb 2026 – Jun 2026</div>
        <ul class="exp-bullets">
          <li>Developed full-stack web applications using Java, Servlets, JSP, HTML, CSS, and MySQL.</li>
          <li>Implemented backend logic with JDBC and performed CRUD operations for dynamic applications.</li>
          <li>Debugged, tested, and optimized application performance while collaborating on end-to-end software development tasks.</li>
        </ul>
      </div>
    </div>
  </section>

  <div class="section-divider"></div>

  <!-- EDUCATION -->
  <section id="education">
    <div class="section-label"><span>04 / Education</span></div>
    <h2>Academic Background</h2>
    <br>
    <div class="edu-grid reveal">

      <div class="edu-card">
        <div class="edu-degree">BE in Computer Science &amp; Engineering</div>
        <div class="edu-school">Malnad College of Engineering</div>
        <p style="font-size:.85rem;color:var(--muted)">Karnataka, India</p>
        <div class="edu-meta">
          <span>Jul 2023 – Jul 2026</span>
          <span class="cgpa">CGPA: 7.46</span>
        </div>
      </div>

      <div class="edu-card">
        <div class="edu-degree">Diploma in Computer Science</div>
        <div class="edu-school">Rajeev Polytechnic</div>
        <p style="font-size:.85rem;color:var(--muted)">Karnataka, India</p>
        <div class="edu-meta">
          <span>Jul 2021 – Jun 2023</span>
          <span class="cgpa">CGPA: 8.8</span>
        </div>
      </div>

    </div>
  </section>

  <div class="section-divider"></div>

  <!-- CONTACT -->
  <section id="contact">
    <div class="section-label" style="justify-content:center"><span>05 / Contact</span></div>
    <h2>Let's Connect</h2>
    <p>
      Open to opportunities, collaborations, and conversations.<br>
      Feel free to reach out any time.
    </p>
    <div class="contact-links reveal">
      <a href="mailto:sohanhg12@gmail.com" class="contact-link">✉ sohanhg12@gmail.com</a>
      <a href="tel:+918150952155" class="contact-link">📞 +91 8150952155</a>
      <a href="https://www.linkedin.com/in/sohan-h-g-331958343/" target="_blank" class="contact-link">in LinkedIn</a>
      <a href="https://github.com/SohanHg" target="_blank" class="contact-link">⌥ GitHub</a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <span>© 2026 Sohan H G</span>
    
  </footer>

  <script>
    // Scroll reveal
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    reveals.forEach(r => observer.observe(r));
  </script>
</body>
</html>
"""

@app.route("/")
def portfolio():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("🚀  Portfolio running at http://127.0.0.1:5000")
    app.run(debug=False, host="0.0.0.0", port=5000)
