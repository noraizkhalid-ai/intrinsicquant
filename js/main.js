/* =============================================
   INTRINSICQUANT — Main JavaScript
   ============================================= */

(function () {
  'use strict';

  /* ── NAV SCROLL BEHAVIOUR ── */
  const nav = document.querySelector('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 60) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  /* ── MOBILE HAMBURGER MENU ── */
  const hamburger = document.querySelector('.nav__hamburger');
  const mobileDrawer = document.querySelector('.nav__mobile');
  if (hamburger && mobileDrawer) {
    hamburger.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.toggle('open');
      hamburger.classList.toggle('open', isOpen);
      hamburger.setAttribute('aria-expanded', isOpen);
    });
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (nav && !nav.contains(e.target) && !mobileDrawer.contains(e.target)) {
        mobileDrawer.classList.remove('open');
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ── ACTIVE NAV LINK ── */
  (function setActiveLink() {
    const path = window.location.pathname.split('/').pop() || 'index.html';
    const links = document.querySelectorAll('.nav__links .nav__link, .nav__mobile .nav__link');
    links.forEach(link => {
      link.classList.remove('active');
      const href = link.getAttribute('href');
      if (href === path || (path === '' && href === 'index.html')) {
        link.classList.add('active');
      }
    });
  })();

  /* ── INTERSECTION OBSERVER — fade-in on scroll ── */
  const observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Enhanced selector for all animatable elements across About and Services pages
  document.querySelectorAll(`.service-cell, .package-card, .step, .blog-card, .team-card, .svc-card, .pain-card, .why-col, .step-item,
    .about-story__quote, .about-story__body, .about-mission__card, .about-different__card, .about-hive__stat,
    .about-values__card, .about-team__card, .hr-coverage__card, .hr-paingain__col, .hr-pricing__card,
    .hr-process__step, .hr-trust__item`).forEach(el => {
    el.classList.add('reveal');
    observer.observe(el);
  });

  /* ── STAGGER ANIMATIONS FOR GRIDS ── */
  const staggerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const children = entry.target.children;
        Array.from(children).forEach((child, index) => {
          setTimeout(() => {
            child.classList.add('is-visible');
          }, index * 100);
        });
        staggerObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.about-different__grid, .about-values__grid, .hr-coverage__grid, .hr-trust__grid').forEach(grid => {
    const children = grid.children;
    Array.from(children).forEach(child => {
      child.classList.add('reveal-stagger-item');
    });
    staggerObserver.observe(grid);
  });

  /* ── ICON ANIMATIONS ── */
  const iconObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-icon');
        iconObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.about-mission__icon, .about-different__icon, .hr-coverage__icon, .hr-trust__icon').forEach(icon => {
    iconObserver.observe(icon);
  });

  /* ── PARALLAX EFFECT FOR HERO SECTIONS ── */
  const heroSections = document.querySelectorAll('.about-hero, .hr-hero');
  if (heroSections.length > 0) {
    window.addEventListener('scroll', () => {
      heroSections.forEach(hero => {
        const scrolled = window.scrollY;
        const heroContent = hero.querySelector('.about-hero__content, .hr-hero__content');
        const heroTexture = hero.querySelector('.about-hero__texture, .hr-hero__texture');

        if (heroContent && scrolled < window.innerHeight) {
          heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
          heroContent.style.opacity = 1 - (scrolled / window.innerHeight);
        }

        if (heroTexture && scrolled < window.innerHeight) {
          heroTexture.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
      });
    }, { passive: true });
  }

  /* ── SECTION LABELS AND TITLES ANIMATION ── */
  const headerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        headerObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.section-label, .hr-hero__label, .about-hero__label').forEach(label => {
    label.classList.add('reveal-label');
    headerObserver.observe(label);
  });

  document.querySelectorAll('.section-title, .hr-hero__headline, .about-hero__headline').forEach(title => {
    title.classList.add('reveal-title');
    headerObserver.observe(title);
  });

  /* ── SMOOTH SCROLL FOR ANCHOR LINKS ── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Close mobile nav if open
        if (mobileDrawer) mobileDrawer.classList.remove('open');
        if (hamburger) { hamburger.classList.remove('open'); hamburger.setAttribute('aria-expanded', 'false'); }
      }
    });
  });



  /* ── COUNTER ANIMATION (Speedometer Effect) ── */
  function animateCounter(el) {
    const target = parseFloat(el.dataset.target);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const duration = 2000; // Slightly longer for better effect
    const start = performance.now();

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);

      // Enhanced speedometer easing: fast start, gradual slow down
      // Using ease-out-quart for more dramatic speedometer effect
      const eased = 1 - Math.pow(1 - progress, 4);

      const current = Math.round(eased * target);
      el.textContent = prefix + current + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        // Ensure we end on exact target value
        el.textContent = prefix + target + suffix;
      }
    }
    requestAnimationFrame(update);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.counted) {
        entry.target.dataset.counted = '1';
        // Small delay for better visual timing
        setTimeout(() => {
          animateCounter(entry.target);
        }, 200);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-counter]').forEach(el => {
    counterObserver.observe(el);
  });

  /* ── FORM VALIDATION (contact page) ── */
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const name = this.querySelector('[name="name"]');
      const email = this.querySelector('[name="email"]');
      const message = this.querySelector('[name="message"]');
      let valid = true;

      [name, email, message].forEach(field => {
        if (field && !field.value.trim()) {
          field.classList.add('error');
          valid = false;
        } else if (field) {
          field.classList.remove('error');
        }
      });

      if (email && email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        email.classList.add('error');
        valid = false;
      }

      if (valid) {
        const btn = this.querySelector('[type="submit"]');
        btn.textContent = 'Message Sent ✓';
        btn.disabled = true;
        btn.style.background = 'rgba(201,168,76,0.3)';
      }
    });
  }

})();
